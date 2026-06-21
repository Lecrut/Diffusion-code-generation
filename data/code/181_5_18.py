import re

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def extract_vowel_words(phrases):
    words_with_vowels = {word for phrase in phrases for word in re.findall(r'\b\w+\b', phrase) if any(char in vowels for char in word)}
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Hello, world!",
        "Python is awesome.",
        "Data science and machine learning are fascinating.",
        "Vowels: aeiouAEIOU"
    ]
    
    result = extract_vowel_words(sample_phrases)
    print(result)