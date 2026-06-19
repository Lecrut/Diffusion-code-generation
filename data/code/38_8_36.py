class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.char_count = {}

    def count_characters(self):
        for char in self.input_string:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1

    def get_unique_characters(self):
        return set(char for char, count in self.char_count.items() if count == 1)

    def get_repeated_characters(self):
        return [char for char, count in self.char_count.items() if count > 1]

if __name__ == '__main__':
    sample_string = "character"
    analyzer = StringAnalyzer(sample_string)
    analyzer.count_characters()
    unique_chars = analyzer.get_unique_characters()
    repeated_chars = analyzer.get_repeated_characters()
    print("Unique Characters:", unique_chars)
    print("Repeated Characters:", repeated_chars)