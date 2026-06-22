def count_character_frequencies(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    frequency_dict = {}
    for char in input_string:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    return frequency_dict

if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = count_character_frequencies(test_string1)
    print(f"Input: '{test_string1}', Output: {result1}")
    
    test_string2 = "Python3.10 is great."
    result2 = count_character_frequencies(test_string2)
    print(f"Input: '{test_string2}', Output: {result2}")
    
    test_string3 = "$$$abc123xyz"
    result3 = count_character_frequencies(test_string3)
    print(f"Input: '{test_string3}', Output: {result3}")
    
    test_string4 = "OnlyLetters"
    result4 = count_character_frequencies(test_string4)
    print(f"Input: '{test_string4}', Output: {result4}")