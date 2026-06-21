class VowelFilter:
    VOULES = {'a', 'e', 'i', 'o', 'u'}

    @staticmethod
    def contains_vowel(word: str) -> bool:
        return any(char in VowelFilter.VOULES for char in word.lower())

    @classmethod
    def filter_words(cls, text: str) -> list[str]:
        words = re.findall(r'\b\w+\b', text.lower())
        return [word for word in words if cls.contains_vowel(word)]

if __name__ == '__main__':
    sample_text = "This is a test sentence with many vowels and consonants. Programming is fun."
    result = VowelFilter.filter_words(sample_text)
    print(result)