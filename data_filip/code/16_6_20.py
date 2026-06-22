def run_length_encode_strings(strings):
    if not strings:
        return []
    
    result = []
    current_string = strings[0]
    count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current_string:
            count += 1
        else:
            result.append((count, current_string))
            current_string = strings[i]
            count = 1
    
    result.append((count, current_string))
    return result

if __name__ == '__main__':
    sample_input = ["a", "a", "b", "b", "b", "c", "a", "a", "a"]
    encoded = run_length_encode_strings(sample_input)
    print(encoded)
    
    sample_input2 = []
    encoded2 = run_length_encode_strings(sample_input2)
    print(encoded2)
    
    sample_input3 = ["hello"]
    encoded3 = run_length_encode_strings(sample_input3)
    print(encoded3)