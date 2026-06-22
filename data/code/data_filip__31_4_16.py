def hex_strings_to_integers(hex_list: list[str]) -> list[int]:
    return [int(h, 16) for h in hex_list]

if __name__ == '__main__':
    sample_hexes = ["ff", "10", "0a", "1234"]
    result = hex_strings_to_integers(sample_hexes)
    print(result)