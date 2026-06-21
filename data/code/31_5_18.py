def hex_to_dec(hex_string):
    clean_hex = hex_string.replace("0x", "").replace("0X", "")
    return int(clean_hex, 16)

if __name__ == '__main__':
    sample_hex_code = "BEEF"
    decimal_value = hex_to_dec(sample_hex_code)
    print(decimal_value)