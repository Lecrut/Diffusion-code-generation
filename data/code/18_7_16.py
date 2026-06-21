def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccccaaa"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_2 = "AABCCCCD"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)