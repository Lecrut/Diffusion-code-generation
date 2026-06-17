def uppercase_char_generator(input_string):
    for char in input_string:
        yield char.upper()
if __name__ == '__main__':
    sample_string = "hello world"
    generator = uppercase_char_generator(sample_string)
    result_list = list(generator)
    print(result_list)
    long_string = "this is a very long string designed to test memory efficiency" * 1000
    generator_long = uppercase_char_generator(long_string)
    result_long = list(generator_long)
    print("--- Long String Test ---")
    print(len(result_long))
    print(result_long[:50])