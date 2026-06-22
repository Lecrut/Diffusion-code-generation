def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count) + current_char)
            else:
                result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(str(count) + current_char)
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    input_string = "aaabbbcc"
    output = compress_string(input_string)
    print(output)