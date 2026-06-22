class LetterFrequencyAnalyzer:
    def __init__(self, text):
        self.text = text
        self.frequency = {}
    
    def count_frequency(self):
        for char in self.text:
            if 'a' <= char.lower() <= 'z':
                lower_char = char.lower()
                self.frequency[lower_char] = self.frequency.get(lower_char, 0) + 1
    
    def get_frequent_letters(self):
        frequent_letters = []
        for letter, count in self.frequency.items():
            if count > 1:
                frequent_letters.append((letter, count))
        return frequent_letters

if __name__ == '__main__':
    sample_string = "Analyze this sentence with multiple letters!"
    analyzer = LetterFrequencyAnalyzer(sample_string)
    analyzer.count_frequency()
    
    result = analyzer.get_frequent_letters()
    for letter, count in result:
        print(f"{letter}: {count}")