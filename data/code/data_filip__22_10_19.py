def compress_rle(s: str) -> str:
    if not s:
        return ""

    compressed_parts = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1

    compressed_parts.append(f"{current_char}{count}")
    return "".join(compressed_parts)

if __name__ == '__main__':
    input_string = "aabcccccaaa"
    result = compress_rle(input_string)
    print(result)