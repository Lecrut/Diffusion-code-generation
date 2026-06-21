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
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char + str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa11122"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    single_char = "z"
    single_result = run_length_encode(single_char)
    print(single_result)
    
    mixed_input = "A111B222C333D444"
    mixed_result = run_length_encode(mixed_input)
    print(mixed_result)