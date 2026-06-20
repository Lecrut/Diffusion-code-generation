import string

def create_vowel_translation_table():
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans(vowels, " " * len(vowels))
    return trans_table

def strip_vowels(text, table):
    return text.translate(table)

if __name__ == "__main__":
    sample_text = "Hello World! This is a sample text with vowels."
    translation_table = create_vowel_translation_table()
    result = strip_vowels(sample_text, translation_table)
    print(result)