def extract_vowels_reverse(phrase):
    vowels = "aeiouAEIOU"
    extracted_vowels = [char for char in phrase if char in vowels]
    return ''.join(extracted_vowels[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_vowels_reverse(sample_phrase))