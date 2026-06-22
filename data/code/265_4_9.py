def extract_vowels_and_reverse(phrase):
    vowels = "aeiouAEIOU"
    extracted_chars = [char for char in phrase if char in vowels]
    return ''.join(extracted_chars[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello World!"
    result = extract_vowels_and_reverse(sample_phrase)
    print(result)