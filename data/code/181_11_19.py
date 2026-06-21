class WordFilter:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def has_vowel(self, word: str) -> bool:
        return any(char in self.vowels for char in word.lower())

    def filter_words(self, text: str) -> list[str]:
        words = re.findall(r'\b\w+\b', text)
        return [word for word in words if self.has_vowel(word)]

if __name__ == '__main__':
    sample_string = "This is a test sentence with some words like programming and education."
    filter_instance = WordFilter()
    result = filter_instance.filter_words(sample_string)
    print(result)