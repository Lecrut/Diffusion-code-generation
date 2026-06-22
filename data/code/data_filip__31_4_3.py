def hex_to_int_list(hex_strings):
    return [int(s, 16) for s in hex_strings]

if __name__ == '__main__':
    sample_data = ["0A", "1F", "FF", "100", "deadbeef"]
    result = hex_to_int_list(sample_data)
    print(result)