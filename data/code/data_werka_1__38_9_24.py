class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string.lower()
        self.char_counts = {}
    
    def count_characters(self):
        for char in self.input_string:
            if char.isalpha():
                self.char_counts[char] = self.char_counts.get(char, 0) + 1
    
    def find_repeated_letters(self):
        repeated_letters = [char for char, count in self.char_counts.items() if count > 1]
        return repeated_letters

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    analyzer = StringAnalyzer(sample_input)
    analyzer.count_characters()
    result = analyzer.find_repeated_letters()
    print(result)