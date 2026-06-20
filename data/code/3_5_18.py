def remove_vowels(text):
    vowels = "aeiouAEIOU"
    table = str.maketrans({vowel: None for vowel in vowels})
    return text.translate(table)

if __name__ == '__main__':
    sample_text = "Hello World"
    print(remove_vowels(sample_text))