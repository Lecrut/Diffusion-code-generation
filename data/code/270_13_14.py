import re

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "This is an example sentence with multiple   spaces."
    result = remove_spaces(sample_text)
    print(result)