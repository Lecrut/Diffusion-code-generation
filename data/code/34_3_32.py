import sys

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    capitalized_text = capitalize_words(sample_input)
    print(capitalized_text)