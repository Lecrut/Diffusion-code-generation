def hex_strings_to_integers(hex_strings: list[str]) -> list[int]:
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hexes = ['0x1a', 'FF', '00', '10', 'deadbeef']
    result = hex_strings_to_integers(sample_hexes)
    print(result)