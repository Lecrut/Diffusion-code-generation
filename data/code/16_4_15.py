def rle_compress(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "AAABBBDDC"
    print(rle_compress(sample1))
    
    sample2 = "ABC"
    print(rle_compress(sample2))
    
    sample3 = "A"
    print(rle_compress(sample3))
    
    sample4 = ""
    print(rle_compress(sample4))
    
    sample5 = "AABBCCDD"
    print(rle_compress(sample5))