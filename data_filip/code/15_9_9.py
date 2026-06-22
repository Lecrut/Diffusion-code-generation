def compress_string(s: str) -> str:
    if not s:
        return ''
    
    compressed_parts = []
    count = 1
    length = len(s)
    
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_parts.append(s[i - 1] + str(count))
            count = 1
    
    compressed_parts.append(s[length - 1] + str(count))
    compressed_str = ''.join(compressed_parts)
    
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)