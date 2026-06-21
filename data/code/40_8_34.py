class StringAnalyzer:
    def __init__(self, strings):
        self.strings = strings

    def get_first_letters(self):
        return [s[0] for s in self.strings if s]

if __name__ == '__main__':
    sample_strings = ['strawberry', 'tangerine', 'ugli fruit', 'vanilla']
    analyzer = StringAnalyzer(sample_strings)
    first_letters = analyzer.get_first_letters()
    print(first_letters)