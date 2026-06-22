import re

def remove_spaces(text):
    return re.sub('\\s+', '', text)
if __name__ == '__main__':
    sample_text = 'Python is a widely-used programming language.'
    no_spaces = remove_spaces(sample_text)
    print(no_spaces)