import string

def replace_spaces_with_underscores(text: str) -> str:
    return text.translate(str.maketrans(' ', '_', ' '))

if __name__ == '__main__':
    sample_input = 'Hello World Python Code'
    result = replace_spaces_with_underscores(sample_input)
    print(result)