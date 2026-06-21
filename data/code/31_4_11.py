def hex_strings_to_integers(hex_strings: list[str]) -> list[int]:
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hex_strings = ["0a", "ff", "100", "dead", "beef"]
    result = hex_strings_to_integers(sample_hex_strings)
    print(result)