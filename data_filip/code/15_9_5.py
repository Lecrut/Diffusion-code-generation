def compress_string(s: str) -> str:
    if not s:
        return s

    compressed_parts = []
    current_char = s[0]
    count = 0

    for char in s:
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(current_char)
            compressed_parts.append(str(count))
            current_char = char
            count = 1

    compressed_parts.append(current_char)
    compressed_parts.append(str(count))

    compressed = ''.join(compressed_parts)

    if len(compressed) < len(s):
        return compressed

    return s

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)