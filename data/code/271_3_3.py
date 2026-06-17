def char_type_generator(input_string):
    for index, char in enumerate(input_string):
        char_type = "letter" if 'a' <= char <= 'z' or 'A' <= char <= 'Z' else "symbol"
        yield (char, char_type)
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    generator = char_type_generator(sample_string)
    for char, char_type in generator:
        print(f"('{char}', '{char_type}')")