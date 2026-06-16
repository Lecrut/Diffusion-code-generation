def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char.upper()
if __name__ == '__main__':
    test_string = "hello world this is a generator"
    generator = letter_generator(test_string)
    result = list(generator)
    print(result)