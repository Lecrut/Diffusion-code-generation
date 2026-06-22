def compress_string(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    compressed.append(current_char)
    compressed.append(str(count))
    result = ''.join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    print(compress_string('aabcccccaaa'))