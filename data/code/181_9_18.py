from typing import List

VOWELS = "aeiouAEIOU"

def filter_vowel_words(sentences: List[str]) -> List[List[str]]:
    return [[word for word in sentence.split() if any(char in VOWELS for char in word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    print(filter_vowel_words(sample_sentences))