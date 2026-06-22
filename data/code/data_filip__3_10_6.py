def remove_vowels(text: str) -> str:
    translation_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_input = 'Hello World'
    result = remove_vowels(sample_input)
    print(result)
    another_sample = 'Python Programming is awesome!'
    result2 = remove_vowels(another_sample)
    print(result2)