class StringAnalyzer:
    IGNORE_CASE = True

    @staticmethod
    def _normalize_char(char):
        if StringAnalyzer.IGNORE_CASE and char.isalpha():
            return char.lower()
        return char

    def __init__(self, input_string):
        self.input_string = input_string

    def check_for_duplicates(self):
        char_count = {}
        for char in self.input_string:
            normalized_char = StringAnalyzer._normalize_char(char)
            if normalized_char in char_count:
                char_count[normalized_char] += 1
            else:
                char_count[normalized_char] = 1

        duplicates = [char for char, count in char_count.items() if count > 1]
        return sorted(duplicates)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Programming"
    analyzer_1 = StringAnalyzer(sample_string_1)
    analyzer_2 = StringAnalyzer(sample_string_2)
    print(analyzer_1.check_for_duplicates())
    print(analyzer_2.check_for_duplicates())