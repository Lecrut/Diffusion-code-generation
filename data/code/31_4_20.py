def hex_to_int_list(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hex_list = ["1a", "ff", "0", "deadbeef", "CAFEBABE"]
    result = hex_to_int_list(sample_hex_list)
    print(result)