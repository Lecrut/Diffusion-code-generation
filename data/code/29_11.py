def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = sum((1 for char in text if char in vowels))
    return count
if __name__ == '__main__':
    sample_text = 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet.'
    vowel_count = count_vowels(sample_text)
    print(vowel_count)