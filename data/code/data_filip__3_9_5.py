import string

TRANSLATION_TABLE = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(text):
    return text.translate(TRANSLATION_TABLE)

if __name__ == '__main__':
    sample_input = "Hello World! Python is Great."
    result = remove_vowels(sample_input)
    print(result)