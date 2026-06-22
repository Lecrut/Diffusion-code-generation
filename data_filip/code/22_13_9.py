def rle_compress_twist(data):
    if not data:
        return ''
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        
        while i + count < n and data[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(str(count))
            result.append(current_char)
        else:
            for _ in range(count):
                result.append(current_char)
        
        i += count
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "aaabbbccc"
    print(rle_compress_twist(sample1))
    
    sample2 = "aabbcc"
    print(rle_compress_twist(sample2))
    
    sample3 = "hello world"
    print(rle_compress_twist(sample3))
    
    sample4 = "aaabbaaacc"
    print(rle_compress_twist(sample4))
    
    sample5 = ""
    print(rle_compress_twist(sample5))
    
    sample6 = "a"
    print(rle_compress_twist(sample6))
    
    sample7 = "aaaabbbbcccd"
    print(rle_compress_twist(sample7))