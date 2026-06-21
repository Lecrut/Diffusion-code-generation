def extract_vowel_words(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word for word in text.lower().split() if any(char in vowels for char in word)}

if __name__ == '__main__':
    sample_text = "This is a test sentence with many words and some consonants like r and t."
    result = extract_vowel_words(sample_text)
    print(result)