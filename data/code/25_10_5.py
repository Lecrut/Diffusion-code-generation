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
            compressed.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    result = "".join(compressed)
    
    if len(result) >= len(s):
        return s
    
    return result

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    print(compress_string(sample_input))
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("abcde"))