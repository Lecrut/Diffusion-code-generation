import string

def remove_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans("", "", vowels)
    return text.translate(translation_table)

if __name__ == "__main__":
    sample_input = "Hello World, this is a Test String"
    result = remove_vowels(sample_input)
    print(result)