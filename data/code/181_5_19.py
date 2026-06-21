import re

def extract_vowel_words(phrases):
    vowels = 'aeiouAEIOU'
    words_with_vowels = set(word for phrase in phrases for word in re.findall(r'\b\w+\b', phrase) if any(vowel in word for vowel in vowels))
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Hello, world!",
        "Python programming is fun.",
        "Data science and machine learning."
    ]
    result = extract_vowel_words(sample_phrases)
    print(result)