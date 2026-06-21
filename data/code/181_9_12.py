from typing import List

class VowelWordFilter:
    def __init__(self):
        self.vowels = "aeiouAEIOU"

    def has_vowel(self, char: str) -> bool:
        return char in self.vowels

    def words_with_vowels(self, sentences: List[str]) -> List[List[str]]:
        result = []
        for sentence in sentences:
            vowel_words = [word for word in sentence.split() if any(self.has_vowel(char) for char in word)]
            result.append(vowel_words)
        return result

if __name__ == '__main__':
    filter_instance = VowelWordFilter()
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    filtered_words = filter_instance.words_with_vowels(sample_sentences)
    print(filtered_words)