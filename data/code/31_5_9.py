BASE_RADIX = 16
SAMPLE_HEX = "DEADBEEF"

def hex_to_decimal(hex_code):
    return int(hex_code, BASE_RADIX)

if __name__ == '__main__':
    value = hex_to_decimal(SAMPLE_HEX)
    print(value)