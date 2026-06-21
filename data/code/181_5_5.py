import re

def extract_vowel_words(phrases):
    vowels = "aeiouAEIOU"
    words_with_vowels = {word for phrase in phrases for word in re.findall(r'\b\w+\b', phrase) if any(char in vowels for char in word)}
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Hello, world!",
        "Python programming is fun.",
        "Data science with Python."
    ]
    result = extract_vowel_words(sample_phrases)
    print(result)