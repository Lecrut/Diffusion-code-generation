class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        seen = set()
        duplicates = set()
        for char in input_string:
            if char in seen:
                duplicates.add(char)
            seen.add(char)
        return list(duplicates)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_string_1 = "hello world"
    test_string_2 = "programming"
    test_string_3 = "abcde"
    test_string_4 = "aabbccddeeff"
    print(f"Duplicates in '{test_string_1}': {analyzer.check_for_duplicates(test_string_1)}")
    print(f"Duplicates in '{test_string_2}': {analyzer.check_for_duplicates(test_string_2)}")
    print(f"Duplicates in '{test_string_3}': {analyzer.check_for_duplicates(test_string_3)}")
    print(f"Duplicates in '{test_string_4}': {analyzer.check_for_duplicates(test_string_4)}")