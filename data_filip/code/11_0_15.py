from collections import Counter

class RepeatedCharacterFinder:
    MINIMUM_REPETITION_COUNT = 2

    @staticmethod
    def get_frequency_map(text: str) -> Counter:
        return Counter(text)

    @staticmethod
    def filter_repeated_items(frequency_map: Counter, threshold: int) -> list:
        return [char for char, count in frequency_map.items() if count >= threshold]

    def find_repeated_characters(self, text: str) -> list:
        if not text:
            return []
        frequency_map = self.get_frequency_map(text)
        repeated_characters = self.filter_repeated_items(frequency_map, self.MINIMUM_REPETITION_COUNT)
        return repeated_characters

if __name__ == '__main__':
    finder = RepeatedCharacterFinder()
    sample_text = "banana"
    result = finder.find_repeated_characters(sample_text)
    print(result)