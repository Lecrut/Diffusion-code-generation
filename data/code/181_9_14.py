from typing import List

VOWELS = set('aeiouAEIOU')

def words_with_vowels(sentences: List[str]) -> List[List[str]]:
    return [[word for word in sentence.split() if any(char in VOWELS for char in word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    print(words_with_vowels(sample_sentences))