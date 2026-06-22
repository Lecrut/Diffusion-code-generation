def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

if __name__ == '__main__':
    result = compress_string('cccccccccc')
    print(result)