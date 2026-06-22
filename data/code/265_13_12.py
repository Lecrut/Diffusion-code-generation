class CharacterFrequencyAnalyzer:
    def __init__(self, phrase):
        self.phrase = phrase
        self.char_count = {}
    
    def count_characters(self):
        for char in self.phrase:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1
    
    def get_most_frequent_chars(self):
        max_count = max(self.char_count.values())
        return [char for char, count in self.char_count.items() if count == max_count]

if __name__ == '__main__':
    analyzer = CharacterFrequencyAnalyzer("hello world")
    analyzer.count_characters()
    result = analyzer.get_most_frequent_chars()
    print(result)