class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string.lower()
    
    def find_repeated_letters(self):
        seen_letters = set()
        repeated_letters = set()
        for char in self.input_string:
            if char.isalpha():
                if char in seen_letters:
                    repeated_letters.add(char)
                else:
                    seen_letters.add(char)
        return list(repeated_letters)

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    analyzer = StringAnalyzer(sample_input)
    result = analyzer.find_repeated_letters()
    print(result)