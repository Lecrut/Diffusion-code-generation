def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == '__main__':
    test_string1 = "hello world 123!"
    result1 = character_frequency(test_string1)
    print(f"Input: '{test_string1}', Output: {result1}")
    
    test_string2 = "python3.10 is great."
    result2 = character_frequency(test_string2)
    print(f"Input: '{test_string2}', Output: {result2}")
    
    test_string3 = "$$$abc123xyz"
    result3 = character_frequency(test_string3)
    print(f"Input: '{test_string3}', Output: {result3}")
    
    test_string4 = "onlyletters"
    result4 = character_frequency(test_string4)
    print(f"Input: '{test_string4}', Output: {result4}")