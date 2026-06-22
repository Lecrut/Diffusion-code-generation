def encode_repeated_chars(text: str) -> str:
    if not text:
        return ""

    encoded = []
    count = 1
    current_char = text[0]

    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)

    return "".join(encoded)

if __name__ == '__main__':
    result = encode_repeated_chars("aaabbc")
    print(result)

    result2 = encode_repeated_chars("abcd")
    print(result2)

    result3 = encode_repeated_chars("a")
    print(result3)