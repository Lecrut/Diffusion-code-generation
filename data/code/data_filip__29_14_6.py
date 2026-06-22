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
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = char
            count = 1
    compressed.append(current_char)
    compressed.append(str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample_values = ["aabcccccaaa", "abcdef", "aaabbbccc", "a", ""]
    for val in sample_values:
        print(compress_string(val))