def rle_compress_special(text):
    if not text:
        return ""
    
    result = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        count = 1
        while i + count < n and text[i + count] == char:
            count += 1
        
        if count >= 3:
            result.append(f"{count}{char}")
        else:
            result.append(char * count)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbcc"
    sample2 = "aabbcc"
    sample3 = "aaabbaacccc"
    sample4 = ""
    sample5 = "abcdef"
    
    print(rle_compress_special(sample1))
    print(rle_compress_special(sample2))
    print(rle_compress_special(sample3))
    print(rle_compress_special(sample4))
    print(rle_compress_special(sample5))