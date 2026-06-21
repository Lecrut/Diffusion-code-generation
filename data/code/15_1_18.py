def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}" if count > 1 else current_char)
            current_char = s[i]
            count = 1
    compressed.append(f"{current_char}{count}" if count > 1 else current_char)
    return "".join(compressed)

if __name__ == '__main__':
    sample = 'aaaaabbbbcccd'
    result = compress_string(sample)
    print(result)