from typing import List

def find_vowel_words(sentences: List[str]) -> List[List[str]]:
    vowels = 'aeiouAEIOU'
    return [[word for word in sentence.split() if any(char in vowels for char in word)] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world from Python",
        "The quick brown fox jumps over the lazy dog",
        "A E I O U a e i o u"
    ]
    print(find_vowel_words(sample_sentences))