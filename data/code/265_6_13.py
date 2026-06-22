def extract_uppercase(input_string):
    result = ''.join(char for char in input_string if char.isupper())
    return result

if __name__ == '__main__':
    sample_string = "This is a Complex STRING with Uppercase letters"
    result = extract_uppercase(sample_string)
    print(result)