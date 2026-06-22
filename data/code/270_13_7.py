import re

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "This is another sample with spaces"
    result = remove_spaces(sample_text)
    print(result)