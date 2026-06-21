def rle_encode_byte_optimized(s):
    if not s:
        return []
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    result = rle_encode_byte_optimized(sample_string)
    print(result)
    
    sample_string2 = "ABC"
    result2 = rle_encode_byte_optimized(sample_string2)
    print(result2)
    
    sample_string3 = ""
    result3 = rle_encode_byte_optimized(sample_string3)
    print(result3)
    
    sample_string4 = "AAAAAAAAAA"
    result4 = rle_encode_byte_optimized(sample_string4)
    print(result4)