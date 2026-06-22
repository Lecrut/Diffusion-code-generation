def remove_vowels(text):
    if not text:
        return text
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans('', '', vowels)
    return text.translate(translation_table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)