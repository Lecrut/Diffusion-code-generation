def decode_rle(encoded_list: list) -> str:
    parts = []
    for char, count in encoded_list:
        parts.append(char * count)
    return "".join(parts)

if __name__ == "__main__":
    encoded_data = [("a", 3), ("b", 2), ("c", 1)]
    result = decode_rle(encoded_data)
    print(result)