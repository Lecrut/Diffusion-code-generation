def rle_compress(string: str) -> str:
    if not string:
        return ""

    result = []
    current_char = string[0]
    count = 1
    length = len(string)

    for i in range(1, length):
        char = string[i]
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char * count)
            current_char = char
            count = 1

    if count > 3:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char * count)

    return "".join(result)

if __name__ == "__main__":
    sample_text = "aaabbccccdd"
    compressed = rle_compress(sample_text)
    print(compressed)