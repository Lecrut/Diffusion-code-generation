def hex_strings_to_integers(hex_list):
    return [int(h, 16) for h in hex_list]

if __name__ == '__main__':
    sample_hexes = ['0xff', '0x10', '0x0a', '0xdeadbeef']
    result = hex_strings_to_integers(sample_hexes)
    print(result)