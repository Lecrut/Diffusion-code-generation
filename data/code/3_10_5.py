import string

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans("", "", vowels)
    return text.translate(translation_table)

if __name__ == "__main__":
    sample_string = "Hello World! This is a Python string with vowels."
    result = remove_vowels(sample_string)
    print(result)