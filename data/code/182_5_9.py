def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    example_string = "Python"
    generator_instance = char_generator(example_string)
    
    for character in generator_instance:
        print(character)