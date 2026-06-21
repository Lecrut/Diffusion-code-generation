import re

def normalize_string(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    words_list = cleaned_string.lower().split()
    return words_list

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with special characters: @#$%^&*()"
    print(normalize_string(sample_string))