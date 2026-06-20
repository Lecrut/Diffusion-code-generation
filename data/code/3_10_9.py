def remove_vowels(s: str) -> str:
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans('', '', vowels)
    return s.translate(translation_table)
if __name__ == '__main__':
    sample_strings = ['Hello World', 'Python Programming', 'AEIOU aeiou', 'Rhythm', 'Beautiful Day', 'xyz123', 'Apple Banana Cherry']
    for sample in sample_strings:
        result = remove_vowels(sample)
        print(result)