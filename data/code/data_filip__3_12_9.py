def remove_vowels(text):
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans("", "", vowels)
    return text.translate(translation_table)

if __name__ == "__main__":
    sample_text = "Hello World! Python is a versatile programming language."
    result = remove_vowels(sample_text)
    print(result)