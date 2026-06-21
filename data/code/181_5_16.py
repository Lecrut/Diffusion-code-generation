import re

def extract_words_with_vowels(phrases):
    vowels = 'aeiouAEIOU'
    words_with_vowels = {word for phrase in phrases for word in re.findall(r'\b\w+\b', phrase) if any(vowel in word for vowel in vowels)}
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Hello, world!",
        "Python is great.",
        "Regular expressions are useful."
    ]
    result = extract_words_with_vowels(sample_phrases)
    print(result)