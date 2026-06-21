def hex_strings_to_integers(hex_strings):
    return [int(s, 16) for s in hex_strings]

if __name__ == '__main__':
    sample_hex_strings = ['0x1a', '0xff', '0x0', '0xdeadbeef']
    result = hex_strings_to_integers(sample_hex_strings)
    print(result)