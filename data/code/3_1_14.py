def strip_vowels(text):
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans('', '', vowels)
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Python Programming"
    sample_text3 = "AEIOU aeiou"
    print(strip_vowels(sample_text1))
    print(strip_vowels(sample_text2))
    print(strip_vowels(sample_text3))