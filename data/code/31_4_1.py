def hex_strings_to_integers(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hexes = ['1a', 'ff', '100', 'deaf', 'cafe']
    result = hex_strings_to_integers(sample_hexes)
    print(result)