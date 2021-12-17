import usb

ID_VENDOR_REALSENSE = 0x8086 # Intel
MANUFACTURER_REALSENSE = "Intel(R) RealSense(TM)"
PRODUCT_REALSENSE = "Intel(R) RealSense(TM)"

usb_devices = usb.core.find(find_all=True)

def is_realsense_device(dev):
    is_same_idVendor = dev.idVendor == ID_VENDOR_REALSENSE
    if not is_same_idVendor:
        return False

    is_same_manufacturer = MANUFACTURER_REALSENSE in dev.manufacturer
    is_same_product = PRODUCT_REALSENSE in dev.product

    return is_same_manufacturer and is_same_product

realsense_devices = list(filter(is_realsense_device, usb_devices))
# print(realsense_devices)

for dev in realsense_devices:
    # print("reset RealSense devices:", dev)
    dev.reset()
