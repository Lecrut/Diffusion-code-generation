def build_translation_table():
    vowels = 'aeiouAEIOU'
    translation_map = str.maketrans(vowels, ' ' * len(vowels))
    return translation_map

def strip_vowels(text):
    table = build_translation_table()
    return text.translate(table)

if __name__ == '__main__':
    sample_text = "Hello World, this is a sample text with vowels."
    result = strip_vowels(sample_text)
    print(result)