def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "wwwwaaadexxxxxx"
    encoded_value = run_length_encode(sample_string)
    print(encoded_value)
    
    empty_string = ""
    empty_encoded = run_length_encode(empty_string)
    print(empty_encoded)
    
    single_char = "a"
    single_encoded = run_length_encode(single_char)
    print(single_encoded)
    
    no_repeat = "abcd"
    no_repeat_encoded = run_length_encode(no_repeat)
    print(no_repeat_encoded)