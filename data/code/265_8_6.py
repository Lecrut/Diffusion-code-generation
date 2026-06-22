def extract_non_vowels_reverse(phrase):
    vowels = "aeiouAEIOU"
    non_vowels = [char for char in phrase if char not in vowels]
    return ''.join(non_vowels[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_non_vowels_reverse(sample_phrase))