def count_character_frequencies(input_string):
    frequencies = {}
    for char in input_string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

if __name__ == '__main__':
    test_string1 = "hello world"
    result1 = count_character_frequencies(test_string1)
    print(f"Input: '{test_string1}', Output: {result1}")

    test_string2 = "Python3.10 is great!"
    result2 = count_character_frequencies(test_string2)
    print(f"Input: '{test_string2}', Output: {result2}")