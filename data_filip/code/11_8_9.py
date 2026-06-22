def get_unique_sorted_twice_occuring_chars(text: str) -> list:
    frequency_map = {}
    for character in text:
        if character in frequency_map:
            frequency_map[character] += 1
        else:
            frequency_map[character] = 1
    
    matching_chars = []
    for char_val, freq in frequency_map.items():
        if freq == 2:
            matching_chars.append(char_val)
    
    matching_chars.sort()
    return matching_chars

if __name__ == '__main__':
    test_data = "success"
    output = get_unique_sorted_twice_occuring_chars(test_data)
    print(output)
    
    test_data_two = "banana"
    output_two = get_unique_sorted_twice_occuring_chars(test_data_two)
    print(output_two)
    
    test_data_three = "aabbccdd"
    output_three = get_unique_sorted_twice_occuring_chars(test_data_three)
    print(output_three)