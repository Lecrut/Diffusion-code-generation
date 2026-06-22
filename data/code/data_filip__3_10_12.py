def remove_vowels(text):
    translation_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_text = 'Hello, World! This is a test string with vowels.'
    result = remove_vowels(sample_text)
    print(result)