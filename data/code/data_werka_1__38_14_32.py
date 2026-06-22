class CharacterFrequencyAnalyzer:
    @staticmethod
    def find_repeated_characters(input_string):
        from collections import Counter
        char_count = Counter(input_string)
        repeated_chars = [char for char, count in char_count.items() if count > 1]
        return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = 'characters'
    result = CharacterFrequencyAnalyzer.find_repeated_characters(sample_string)
    print(result)