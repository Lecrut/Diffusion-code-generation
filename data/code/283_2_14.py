class StringChecker:
    def __init__(self, string_list):
        self.string_list = string_list

    def count_non_string_elements(self):
        non_string_count = sum(not isinstance(item, str) for item in self.string_list)
        return non_string_count

if __name__ == '__main__':
    sample_list = ["Hello", 123, "world", True, None, "Python"]
    checker = StringChecker(sample_list)
    result = checker.count_non_string_elements()
    print(result)