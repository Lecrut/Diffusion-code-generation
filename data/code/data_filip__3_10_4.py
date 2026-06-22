def remove_vowels(text: str) -> str:
    translation_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_string = 'Hello World!'
    result = remove_vowels(sample_string)
    print(result)
    another_sample = 'Python Programming'
    another_result = remove_vowels(another_sample)
    print(another_result)
    empty_string = ''
    empty_result = remove_vowels(empty_string)
    print(empty_result)
    no_vowels = 'Rhythm'
    no_vowels_result = remove_vowels(no_vowels)
    print(no_vowels_result)
    all_vowels = 'AEIOU aeiou'
    all_vowels_result = remove_vowels(all_vowels)
    print(all_vowels_result)