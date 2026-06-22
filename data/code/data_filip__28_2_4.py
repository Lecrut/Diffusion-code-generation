def rle_encode(data: str) -> str:
    result = []
    current_char = None
    count = 0
    for char in data:
        if char == current_char:
            count += 1
        else:
            if current_char is not None:
                result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    if current_char is not None:
        result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    long_string = "AAAAABBBCCD"
    encoded = rle_encode(long_string)
    print(encoded)