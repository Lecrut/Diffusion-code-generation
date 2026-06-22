def extract_reverse_vowels(phrase):
    vowels = "aeiouAEIOU"
    extracted = [char for char in phrase if char in vowels]
    return ''.join(extracted[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_reverse_vowels(sample_phrase))