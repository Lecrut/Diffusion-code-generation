def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = text[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_2 = "A"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)
    
    sample_input_3 = ""
    encoded_result_3 = run_length_encode(sample_input_3)
    print(encoded_result_3)