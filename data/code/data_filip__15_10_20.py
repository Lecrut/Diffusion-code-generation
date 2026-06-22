def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    n = len(s)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            result.append(str(count))
            count = 1
    
    result.append(s[n - 1])
    result.append(str(count))
    
    compressed = "".join(result)
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == '__main__':
    sample_input = "aaabbbccccca"
    print(compress_string(sample_input))
    
    sample_input_2 = "abcdef"
    print(compress_string(sample_input_2))
    
    sample_input_3 = ""
    print(compress_string(sample_input_3))
    
    sample_input_4 = "aaaa"
    print(compress_string(sample_input_4))