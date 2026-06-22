def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
            
    result.append(current_char + str(count))
    
    compressed = "".join(result)
    
    if len(compressed) >= len(s):
        return s
        
    return compressed

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    print(compress_string(sample_string))