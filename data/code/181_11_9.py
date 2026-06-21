class WordFilter:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def contains_vowel(self, word: str) -> bool:
        return any(char in self.vowels for char in word)

    def filter_vowel_words(self, text: str) -> list:
        words = re.findall(r'\b\w+\b', text.lower())
        return [word for word in words if self.contains_vowel(word)]

if __name__ == '__main__':
    sample_text = "This is a test sentence with many vowels and consonants. Programming is fun."
    filter_instance = WordFilter()
    result = filter_instance.filter_vowel_words(sample_text)
    print(result)