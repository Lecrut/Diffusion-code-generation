TRANSLATION_TABLE = str.maketrans("", "", "aeiouAEIOU")

def remove_vowels(text: str) -> str:
    return text.translate(TRANSLATION_TABLE)

if __name__ == "__main__":
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)