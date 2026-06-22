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
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_strings = [
        "aabcccccaaa",
        "abcdef",
        "aaaaa",
        "ababab",
        "",
        "a"
    ]
    for sample in sample_strings:
        result = compress_string(sample)
        print(f"{sample!r} -> {result!r}")