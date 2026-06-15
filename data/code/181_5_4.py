def vowel_generator(input_string):
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            yield char
if __name__ == '__main__':
    test_string = "Programming is fun and long"
    generator = vowel_generator(test_string)
    result = list(generator)
    print(result)