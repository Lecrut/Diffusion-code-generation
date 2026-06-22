def compress_string(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1
    compressed.append(current_char + str(count))
    result = "".join(compressed)
    if len(result) >= len(s):
        return s
    return result

if __name__ == '__main__':
    sample_input = 'aabcccccaaa'
    result = compress_string(sample_input)
    print(result)