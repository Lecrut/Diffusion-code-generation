def hex_strings_to_integers(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_data = ["1a", "ff", "0", "deadbeef", "A1B2C3"]
    result = hex_strings_to_integers(sample_data)
    print(result)