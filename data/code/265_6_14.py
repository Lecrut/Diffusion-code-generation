def extract_uppercase(input_string):
    return ''.join(char for char in input_string if char.isupper())

if __name__ == '__main__':
    sample_string = "Hello World! This is a Test."
    result = extract_uppercase(sample_string)
    print(result)