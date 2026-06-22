def extract_uppercase(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return ''.join(char for char in input_string if char.isupper())

if __name__ == '__main__':
    sample_string = "This is a Complex String With Uppercase Letters ABC and Mixed abc123!"
    result = extract_uppercase(sample_string)
    print(result)