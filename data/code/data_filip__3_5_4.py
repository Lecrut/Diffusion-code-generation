import string

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans(vowels, " " * len(vowels))
    return text.translate(translation_table).replace(" ", "")

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test String."
    result = remove_vowels(sample_text)
    print(result)