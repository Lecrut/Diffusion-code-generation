def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f"{data[i - 1]}{count}")
            count = 1
    
    result.append(f"{data[length - 1]}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDEEE"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    
    sample_input_2 = "A"
    encoded_output_2 = run_length_encode(sample_input_2)
    print(encoded_output_2)
    
    sample_input_3 = ""
    encoded_output_3 = run_length_encode(sample_input_3)
    print(encoded_output_3)
    
    sample_input_4 = "AABBCCD"
    encoded_output_4 = run_length_encode(sample_input_4)
    print(encoded_output_4)