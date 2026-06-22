def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = char
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    result = run_length_encode(sample_string)
    print(result)
    
    another_sample = "ABC"
    result2 = run_length_encode(another_sample)
    print(result2)
    
    empty_sample = ""
    result3 = run_length_encode(empty_sample)
    print(result3)
    
    single_char = "Z"
    result4 = run_length_encode(single_char)
    print(result4)
    
    complex_sample = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result5 = run_length_encode(complex_sample)
    print(result5)