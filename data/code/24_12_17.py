def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_result.append(f"{count}{current_char}")
            current_char = input_string[i]
            count = 1
    
    encoded_result.append(f"{count}{current_char}")
    return "".join(encoded_result)

if __name__ == '__main__':
    sample_data = "AAABBBCCCCDDDDAAAA"
    compressed_version = run_length_encode(sample_data)
    print(f"Original: {sample_data}")
    print(f"Compressed: {compressed_version}")