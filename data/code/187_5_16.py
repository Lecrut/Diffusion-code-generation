class StringFinder:
    def __init__(self, strings):
        self.strings = strings

    def find_largest_string_by_length(self):
        return max(self.strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    finder = StringFinder(sample_strings)
    largest_string = finder.find_largest_string_by_length()
    print(largest_string)