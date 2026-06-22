import re

def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def remove_spaces(text):
    validate_input(text)
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "This is a sample sentence with extra spaces"
    print(remove_spaces(sample_text))