class ConsonantCounter:
    VOWELS = frozenset('aeiouAEIOU')

    @staticmethod
    def _is_consonant(char: str) -> bool:
        return char.isalpha() and char not in ConsonantCounter.VOWELS

    @staticmethod
    def count(text: str) -> int:
        total = 0
        for char in text:
            if ConsonantCounter._is_consonant(char):
                total += 1
        return total

if __name__ == '__main__':
    sample_data = "Skyline Architects, Inc. - Q3 Report (2024)"
    print(ConsonantCounter.count(sample_data))