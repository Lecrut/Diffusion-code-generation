def compress_string(s):
    if not s:
        return ''
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    compressed.append(str(count) + current_char)
    return ''.join(compressed)

if __name__ == '__main__':
    sample_input = "aaabbcceeee"
    result = compress_string(sample_input)
    print(result)