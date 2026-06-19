import sys

def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_input = "this is a test input"
    result = capitalize_first_letter(sample_input)
    print(result)