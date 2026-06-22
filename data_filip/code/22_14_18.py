def compress_string(s):
    if not s:
        return s
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("aa"))
    print(compress_string("aaa"))