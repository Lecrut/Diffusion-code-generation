def hex_to_decimal(hex_list):
    return [int(h, 16) for h in hex_list]

if __name__ == '__main__':
    sample_values = ["1A", "FF", "100", "DEADBEEF", "0"]
    result = hex_to_decimal(sample_values)
    print(result)