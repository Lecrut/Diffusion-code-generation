TRANSLATION_TABLE = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(text):
    return text.translate(TRANSLATION_TABLE)

if __name__ == '__main__':
    sample_text = "Hello World! This is a Python utility."
    result = remove_vowels(sample_text)
    print(result)