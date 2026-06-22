def run_length_encode(text: str) -> list:
    if not text:
        return []
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    input_str = "aabcccccaaa"
    encoded_result = run_length_encode(input_str)
    print(encoded_result)
    
    input_str_2 = "abc"
    encoded_result_2 = run_length_encode(input_str_2)
    print(encoded_result_2)
    
    input_str_3 = ""
    encoded_result_3 = run_length_encode(input_str_3)
    print(encoded_result_3)
    
    input_str_4 = "a"
    encoded_result_4 = run_length_encode(input_str_4)
    print(encoded_result_4)