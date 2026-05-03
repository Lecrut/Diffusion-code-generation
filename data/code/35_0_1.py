def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string = "Hello World, this is a test string."
    result = count_vowels(test_string)
    print(result)