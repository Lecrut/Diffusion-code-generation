class CharacterFrequencyAnalyzer:
    @staticmethod
    def count_characters(phrase):
        char_count = {}
        for char in phrase:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    @staticmethod
    def find_most_frequent_chars(char_count):
        max_count = max(char_count.values())
        return [char for char, count in char_count.items() if count == max_count]

if __name__ == '__main__':
    sample_phrase = "hello world"
    analyzer = CharacterFrequencyAnalyzer()
    char_count = analyzer.count_characters(sample_phrase)
    most_frequent_chars = analyzer.find_most_frequent_chars(char_count)
    print(most_frequent_chars)