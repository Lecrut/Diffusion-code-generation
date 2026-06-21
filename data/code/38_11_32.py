class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def check_for_duplicates(self):
        char_count = {}
        for char in self.input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        duplicates = [char for char, count in char_count.items() if count > 1]
        return duplicates

if __name__ == '__main__':
    sample_string = "repetition"
    analyzer = StringAnalyzer(sample_string)
    print(analyzer.check_for_duplicates())