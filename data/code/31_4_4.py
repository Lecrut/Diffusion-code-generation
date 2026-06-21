def hex_strings_to_integers(hex_strings: list[str]) -> list[int]:
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    samples = ['0x1A', 'FF', '0', '10', 'deadBEEF']
    result = hex_strings_to_integers(samples)
    print(result)