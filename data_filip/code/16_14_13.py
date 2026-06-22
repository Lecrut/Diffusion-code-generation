def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f"{count}{data[i - 1]}")
            count = 1
    
    result.append(f"{count}{data[length - 1]}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAAAABCCCCDDDDEEEFGGGGG"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_2 = "1222333444455555"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)
    
    empty_input = ""
    encoded_result_3 = run_length_encode(empty_input)
    print(encoded_result_3)