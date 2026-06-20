def remove_vowels(text):
    translation_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))