def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
            
    result.append(str(count) + current_char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)
    
    empty_string = ""
    encoded_empty = run_length_encode(empty_string)
    print(encoded_empty)
    
    single_char = "A"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)
    
    mixed_string = "Hello World!!!"
    encoded_mixed = run_length_encode(mixed_string)
    print(encoded_mixed)