def run_length_encode(input_list):
    if not input_list:
        return []
    
    result = []
    current_string = input_list[0]
    count = 1
    
    for i in range(1, len(input_list)):
        if input_list[i] == current_string:
            count += 1
        else:
            result.append((current_string, count))
            current_string = input_list[i]
            count = 1
    
    result.append((current_string, count))
    
    return result

if __name__ == '__main__':
    sample_list = ["apple", "apple", "banana", "banana", "banana", "cherry", "apple"]
    encoded_result = run_length_encode(sample_list)
    print(encoded_result)