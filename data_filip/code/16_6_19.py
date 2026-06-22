def run_length_encode(input_list):
    if not input_list:
        return []
    
    encoded = []
    current_item = input_list[0]
    count = 1
    
    for i in range(1, len(input_list)):
        item = input_list[i]
        if item == current_item:
            count += 1
        else:
            encoded.append((current_item, count))
            current_item = item
            count = 1
    
    encoded.append((current_item, count))
    
    return encoded

if __name__ == '__main__':
    sample_list = ["apple", "apple", "banana", "banana", "banana", "cherry"]
    result = run_length_encode(sample_list)
    print(result)