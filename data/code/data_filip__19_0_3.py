def compress_rle(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count == 1:
                result.append(current_char)
            else:
                result.append(str(count))
                result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count == 1:
        result.append(current_char)
    else:
        result.append(str(count))
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    compressed_result = compress_rle(sample_input)
    print(compressed_result)