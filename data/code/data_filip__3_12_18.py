import string

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    translation_map = str.maketrans("", "", vowels)
    return text.translate(translation_map)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)