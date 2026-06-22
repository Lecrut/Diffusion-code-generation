class StringAnalyzer:
    def __init__(self, text):
        self.text = text

    def check_for_duplicates(self):
        char_count = {}
        for char in self.text:
            if char.isalpha():
                lower_char = char.lower()
                char_count[lower_char] = char_count.get(lower_char, 0) + 1
        duplicates = {char for char, count in char_count.items() if count > 1}
        return duplicates

if __name__ == '__main__':
    sample_text_1 = "hello world"
    sample_text_2 = "programming"
    sample_text_3 = "aabbccddeeffg"
    sample_text_4 = "unique"

    analyzer_1 = StringAnalyzer(sample_text_1)
    print(analyzer_1.check_for_duplicates())

    analyzer_2 = StringAnalyzer(sample_text_2)
    print(analyzer_2.check_for_duplicates())

    analyzer_3 = StringAnalyzer(sample_text_3)
    print(analyzer_3.check_for_duplicates())

    analyzer_4 = StringAnalyzer(sample_text_4)
    print(analyzer_4.check_for_duplicates())