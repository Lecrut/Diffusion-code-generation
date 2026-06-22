def run_length_encode(input_string):
    if not input_string:
        return ""
    
    compressed = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = input_string[i]
            count = 1
    
    compressed.append(f"{count}{current_char}")
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    result = run_length_encode(sample_input)
    print(result)