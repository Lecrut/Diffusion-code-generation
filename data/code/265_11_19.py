def count_character_frequencies(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = count_character_frequencies(test_string1)
    print(f"Input: '{test_string1}', Output: {result1}")
    
    test_string2 = "Python3.10 is great."
    result2 = count_character_frequencies(test_string2)
    print(f"Input: '{test_string2}', Output: {result2}")