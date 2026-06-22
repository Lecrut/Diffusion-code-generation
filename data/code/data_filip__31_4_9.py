def hex_strings_to_integers(hex_strings):
    return [int(s, 16) for s in hex_strings]

if __name__ == '__main__':
    sample_hex_list = ["ff", "0a", "1a2b3c", "deadbeef", "0", "123"]
    result = hex_strings_to_integers(sample_hex_list)
    print(result)