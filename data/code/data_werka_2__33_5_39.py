def is_non_whitespace(char):
    return not char.isspace()

def non_whitespace_generator(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    for char in input_string:
        if is_non_whitespace(char):
            yield char

if __name__ == '__main__':
    sample_input = "Hello World"
    result = ''.join(non_whitespace_generator(sample_input))
    print(result)