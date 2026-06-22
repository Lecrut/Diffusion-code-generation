def remove_vowels(s):
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans("", "", vowels)
    return s.translate(translation_table)

if __name__ == "__main__":
    sample_text = "Hello World! This is an Example String."
    result = remove_vowels(sample_text)
    print(result)