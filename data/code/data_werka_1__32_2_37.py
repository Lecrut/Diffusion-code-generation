def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def get_length_of_string(text):
    validate_input(text)
    return len(text)

if __name__ == '__main__':
    sample_string = 'Hello World'
    print(get_length_of_string(sample_string))