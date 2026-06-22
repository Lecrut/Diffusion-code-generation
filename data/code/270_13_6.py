import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def remove_spaces(text):
    validate_input(text)
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "This is a sample sentence with extra spaces"
    print(remove_spaces(sample_text))