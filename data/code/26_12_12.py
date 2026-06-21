def compress_string(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    encoded = "".join(result)
    return encoded if len(encoded) < len(s) else s

if __name__ == "__main__":
    print(compress_string(""))
    print(compress_string("A"))
    print(compress_string("AAABBBCC"))
    print(compress_string("ABCDE"))
    print(compress_string("AABBCCC"))
    print(compress_string("AAAAAAAAAA"))