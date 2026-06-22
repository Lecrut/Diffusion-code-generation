def is_valid_string(input_string):
    return isinstance(input_string, str)

def reverse_words(input_string):
    if not is_valid_string(input_string):
        raise ValueError("Input must be a string")
    
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Hello world from Python"
    try:
        result = reverse_words(sample_input)
        print(result)
    except ValueError as e:
        print(e)