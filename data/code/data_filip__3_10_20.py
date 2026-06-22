def remove_vowels(text):
    translation_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_strings = ['Hello World', 'Python Programming', 'AEIOU aeiou', 'No vowels here!', 'The quick brown fox jumps over the lazy dog', '', '12345 !@#$%', 'Rhythm', 'Beautiful day']
    for sample in sample_strings:
        result = remove_vowels(sample)
        print(f"Input:  '{sample}'")
        print(f"Output: '{result}'")
        print()