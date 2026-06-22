def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)
    
    sample_string2 = "ABC"
    result2 = run_length_encode(sample_string2)
    print(result2)
    
    sample_string3 = "AAAAAAAAAA"
    result3 = run_length_encode(sample_string3)
    print(result3)