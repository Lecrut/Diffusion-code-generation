def rle_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    print(rle_encode("aaabbbccca"))
    print(rle_encode("abc"))
    print(rle_encode("a"))
    print(rle_encode(""))
    print(rle_encode("aaaa"))