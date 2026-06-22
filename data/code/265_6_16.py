def is_uppercase(char):
    return char.isupper()

def extract_uppercase(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return ''.join(filter(is_uppercase, input_string))

if __name__ == '__main__':
    sample_string = "This is a complex String with Uppercase letters ABC and lowercase."
    result = extract_uppercase(sample_string)
    print(result)