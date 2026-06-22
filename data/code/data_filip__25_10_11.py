def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    length = len(s)
    
    for i in range(length):
        if i + 1 < length and s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    
    result = "".join(compressed)
    if len(result) >= len(s):
        return s
    return result

if __name__ == '__main__':
    sample_input = "aaabbbcccc"
    print(compress_string(sample_input))