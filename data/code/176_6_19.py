import re

def normalize_string(input_str):
    cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    words_list = cleaned_str.lower().split()
    return words_list

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test string with special characters: @#$%^&*()"
    result = normalize_string(sample_input)
    print(result)