from typing import List

def contains_vowels(word: str) -> bool:
    vowels = "aeiouAEIOU"
    return any(char in vowels for char in word)

def filter_vowel_words(sentences: List[str]) -> List[List[str]]:
    return [[word for word in sentence.split() if contains_vowels(word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    result = filter_vowel_words(sample_sentences)
    print(result)