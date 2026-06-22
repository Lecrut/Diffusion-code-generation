import re

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "Python programming is fun!"
    cleaned_text = remove_spaces(sample_text)
    print(cleaned_text)