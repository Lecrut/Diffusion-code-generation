TRANSLATION_TABLE = str.maketrans('', '', 'aeiouAEIOU')

def strip_vowels(text):
    return text.translate(TRANSLATION_TABLE)

if __name__ == '__main__':
    sample_text = "Hello World, this is a Python script!"
    result = strip_vowels(sample_text)
    print(result)