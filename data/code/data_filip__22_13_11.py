def rle_compress(text):
    if not text:
        return ""
    
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        current_char = text[i]
        count = 1
        
        while i + count < n and text[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(str(count) + current_char)
        else:
            result.append(current_char * count)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbcccdde"
    sample2 = "aabbbccccdddd"
    sample3 = "xyz"
    sample4 = "aaaaabbbbbcc"
    sample5 = ""
    sample6 = "aabbcccdddeeeff"
    
    print(rle_compress(sample1))
    print(rle_compress(sample2))
    print(rle_compress(sample3))
    print(rle_compress(sample4))
    print(rle_compress(sample5))
    print(rle_compress(sample6))