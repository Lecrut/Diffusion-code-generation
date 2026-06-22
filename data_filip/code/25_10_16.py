def compress_string(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    compressed = compress_string(sample_input)
    print(compressed)