class StringAnalyzer:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def check_for_duplicates(self):
        char_count = {}
        duplicates = set()
        for char in self.input_string:
            if char in char_count:
                duplicates.add(char)
            else:
                char_count[char] = 1
        return list(duplicates)

if __name__ == '__main__':
    sample_string = "programming"
    analyzer = StringAnalyzer(sample_string)
    print(analyzer.check_for_duplicates())