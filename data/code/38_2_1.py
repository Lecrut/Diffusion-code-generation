class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        seen = set()
        duplicates = set()
        for char in input_string:
            if char in seen:
                duplicates.add(char)
            seen.add(char)
        return sorted(list(duplicates))
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_string_1 = "hello world"
    test_string_2 = "programming"
    test_string_3 = "abcde"
    test_string_4 = "aabbccddeeff"
    result_1 = analyzer.check_for_duplicates(test_string_1)
    print(f"Input: '{test_string_1}', Duplicates: {result_1}")
    result_2 = analyzer.check_for_duplicates(test_string_2)
    print(f"Input: '{test_string_2}', Duplicates: {result_2}")
    result_3 = analyzer.check_for_duplicates(test_string_3)
    print(f"Input: '{test_string_3}', Duplicates: {result_3}")
    result_4 = analyzer.check_for_duplicates(test_string_4)
    print(f"Input: '{test_string_4}', Duplicates: {result_4}")