import re

VOWELS = set("aeiou")

def find_vowel_words(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    vowel_words = [word for word in words if any(char in VOWELS for char in word)]
    return vowel_words

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with many vowels and consonants."
    result = find_vowel_words(sample_sentence)
    print(result)