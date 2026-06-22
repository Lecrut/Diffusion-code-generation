def hex_strings_to_integers(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hex = ['0x1a', 'ff', '2A', '00', '10']
    print(hex_strings_to_integers(sample_hex))