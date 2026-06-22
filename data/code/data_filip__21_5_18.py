def run_length_encode(s):
    if not s:
        return []
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbcdd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    
    empty_string = ""
    empty_result = run_length_encode(empty_string)
    print(empty_result)
    
    single_char = "z"
    single_result = run_length_encode(single_char)
    print(single_result)
    
    mixed_string = "AABBCCDD"
    mixed_result = run_length_encode(mixed_string)
    print(mixed_result)