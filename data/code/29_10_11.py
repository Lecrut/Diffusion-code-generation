def encode_repeated_chars(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1

    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    print(encode_repeated_chars("aabcccccaaa"))
    print(encode_repeated_chars("abcdef"))
    print(encode_repeated_chars(""))
    print(encode_repeated_chars("a"))
    print(encode_repeated_chars("aaa"))