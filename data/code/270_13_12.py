import re

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    processed_text = remove_spaces(sample_text)
    print(processed_text)