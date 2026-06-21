class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def check_for_duplicates(self):
        char_count = {}
        duplicates = set()
        
        for char in self.input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char, count in char_count.items():
            if count > 1:
                duplicates.add(char)
        
        return list(duplicates)

if __name__ == '__main__':
    sample_string_1 = "hello world"
    sample_string_2 = "programming"
    sample_string_3 = "aabbccddeeffg"
    sample_string_4 = "unique"

    analyzer_1 = StringAnalyzer(sample_string_1)
    print(analyzer_1.check_for_duplicates())

    analyzer_2 = StringAnalyzer(sample_string_2)
    print(analyzer_2.check_for_duplicates())

    analyzer_3 = StringAnalyzer(sample_string_3)
    print(analyzer_3.check_for_duplicates())

    analyzer_4 = StringAnalyzer(sample_string_4)
    print(analyzer_4.check_for_duplicates())