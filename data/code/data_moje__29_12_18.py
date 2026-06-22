class VowelCounter:
    VOWELS = frozenset('aeiouAEIOU')

    @staticmethod
    def count(text: str) -> int:
        return sum(1 for char in text if char in VowelCounter.VOWELS)

if __name__ == '__main__':
    text = "The quick brown fox jumps over the lazy dog"
    result = VowelCounter.count(text)
    print(result)