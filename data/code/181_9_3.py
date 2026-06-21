from typing import List

def find_words_with_vowels(sentences: List[str]) -> List[List[str]]:
    vowels = "aeiouAEIOU"
    return [[word for word in sentence.split() if any(char in vowels for char in word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "Vowels are important in English"
    ]
    print(find_words_with_vowels(sample_sentences))