def hex_to_dec(hex_code): return int(hex_code, 16)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_dec(sample_hex)
    print(result)