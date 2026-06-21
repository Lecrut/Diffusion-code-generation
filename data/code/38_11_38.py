class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string.lower()

    def count_characters(self):
        char_count = {}
        for char in self.input_string:
            if 'a' <= char <= 'z':
                char_count[char] = char_count.get(char, 0) + 1
        return char_count

    def check_for_duplicates(self):
        char_count = self.count_characters()
        duplicates = [char for char, count in char_count.items() if count > 1]
        return sorted(duplicates)

if __name__ == '__main__':
    sample_string_1 = "Programming"
    sample_string_2 = "hello world"
    sample_string_3 = "unique"
    sample_string_4 = "aabbccddeeffg"

    analyzer_1 = StringAnalyzer(sample_string_1)
    print(analyzer_1.check_for_duplicates())

    analyzer_2 = StringAnalyzer(sample_string_2)
    print(analyzer_2.check_for_duplicates())

    analyzer_3 = StringAnalyzer(sample_string_3)
    print(analyzer_3.check_for_duplicates())

    analyzer_4 = StringAnalyzer(sample_string_4)
    print(analyzer_4.check_for_duplicates())