def rle_compress_twist(data):
    if not data:
        return ""
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        while i + count < n and data[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(f"{current_char}{count}")
        else:
            result.append(current_char * count)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbcddde"
    sample2 = "aabbcc"
    sample3 = "aaaabbbbccccddd"
    sample4 = ""
    sample5 = "a"
    sample6 = "aa"
    sample7 = "aaabbbaaa"
    
    print(rle_compress_twist(sample1))
    print(rle_compress_twist(sample2))
    print(rle_compress_twist(sample3))
    print(rle_compress_twist(sample4))
    print(rle_compress_twist(sample5))
    print(rle_compress_twist(sample6))
    print(rle_compress_twist(sample7))