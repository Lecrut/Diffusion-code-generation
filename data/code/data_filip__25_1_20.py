def compress_string(s):
    if not s:
        return ''
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        count = 1
        while i + count < n and s[i + count] == char:
            count += 1
        
        if count == 1:
            result.append(char)
        else:
            result.append(str(count))
            result.append(char)
        
        i += count
    
    return ''.join(result)

if __name__ == '__main__':
    s = 'aaabbbccc'
    compressed = compress_string(s)
    print(compressed)
    
    s2 = 'abc'
    compressed2 = compress_string(s2)
    print(compressed2)