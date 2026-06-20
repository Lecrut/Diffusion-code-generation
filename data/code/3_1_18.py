def create_vowel_remover_table():
    vowels = "aeiouAEIOU"
    translation_map = {char: None for char in vowels}
    return str.maketrans(translation_map)

def strip_vowels(text):
    table = create_vowel_remover_table()
    return text.translate(table)

if __name__ == '__main__':
    sample_text = "Hello World! This is an Example."
    result = strip_vowels(sample_text)
    print(result)