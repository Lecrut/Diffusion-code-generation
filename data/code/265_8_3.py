def extract_non_vowels_reverse(phrase):
    vowels = 'aeiouAEIOU'
    non_vowel_chars = [char for char in phrase if char not in vowels]
    return ''.join(non_vowel_chars[::-1])
if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    result = extract_non_vowels_reverse(sample_phrase)
    print(result)