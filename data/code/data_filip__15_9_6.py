def compress_string(s: str) -> str:
    if not s:
        return s
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    compressed.append(s[-1] + str(count))
    compressed_string = ''.join(compressed)
    
    return compressed_string if len(compressed_string) < len(s) else s

if __name__ == '__main__':
    input_string = 'aabcccccaaa'
    result = compress_string(input_string)
    print(result)