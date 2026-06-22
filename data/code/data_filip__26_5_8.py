def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = input_string[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccccccdddeeeeee"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    unicode_sample = "αααββγγγγδδδδδ"
    unicode_encoded = run_length_encode(unicode_sample)
    print(unicode_encoded)