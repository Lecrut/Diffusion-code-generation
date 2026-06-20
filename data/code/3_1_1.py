def strip_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans("", "", vowels)
    return text.translate(translation_table)

if __name__ == "__main__":
    sample_text = "Hello World"
    result = strip_vowels(sample_text)
    print(result)