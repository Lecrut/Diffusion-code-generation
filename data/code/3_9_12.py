TRANSLATION_TABLE = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(text):
    return text.translate(TRANSLATION_TABLE)

if __name__ == '__main__':
    sample_string = "Hello World! This is a Test."
    result = remove_vowels(sample_string)
    print(result)