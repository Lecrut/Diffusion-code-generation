def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char.isalnum():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = count_character_frequency(test_string1)
    print(f"Input: '{test_string1}', Output: {result1}")
    
    test_string2 = "Python3.10 is great."
    result2 = count_character_frequency(test_string2)
    print(f"Input: '{test_string2}', Output: {result2}")
    
    test_string3 = "$$$abc123xyz"
    result3 = count_character_frequency(test_string3)
    print(f"Input: '{test_string3}', Output: {result3}")
    
    test_string4 = "OnlyLetters"
    result4 = count_character_frequency(test_string4)
    print(f"Input: '{test_string4}', Output: {result4}")