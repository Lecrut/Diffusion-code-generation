def uppercase_char_generator(input_string):
    for char in input_string:
        yield char.upper()
if __name__ == '__main__':
    test_string = "hello world"
    generator = uppercase_char_generator(test_string)
    result_list = list(generator)
    print(result_list)
    long_string = "this is a very long string to test memory efficiency" * 10000
    generator_long = uppercase_char_generator(long_string)
    result_long = list(generator_long)
    print("--- Long String Test (First 20 chars) ---")
    print(result_long[:20])