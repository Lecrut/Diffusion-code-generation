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
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    sample_strings = [
        "aabcccccaaa",
        "abcdef",
        "aaabbbaaa",
        "a",
        "",
        "aaaaaaaaaabb"
    ]
    
    for s in sample_strings:
        print(compress_string(s))