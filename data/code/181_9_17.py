from typing import List

class VowelWordFilter:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def contains_vowels(word: str) -> bool:
        return any(char in VowelWordFilter.VOWELS for char in word)

    @classmethod
    def filter_words_with_vowels(cls, sentences: List[str]) -> List[List[str]]:
        return [[word for word in sentence.split() if cls.contains_vowels(word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    result = VowelWordFilter.filter_words_with_vowels(sample_sentences)
    print(result)