def remove_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans(vowels, None)
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)