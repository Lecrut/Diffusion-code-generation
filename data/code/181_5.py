def vowel_generator(s):
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            yield char
if __name__ == '__main__':
    test_string = "programmingisawesome"
    generator = vowel_generator(test_string)
    result = list(generator)
    print(result)