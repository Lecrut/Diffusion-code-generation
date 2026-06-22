import re

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "This is a sample sentence with extra spaces"
    print(remove_spaces(sample_text))