class StringIntegerFinder:
    def find_smallest_int_string(self, strings):
        return min(strings, key=int)

if __name__ == '__main__':
    finder = StringIntegerFinder()
    sample_strings = ["3", "15", "2", "9"]
    result = finder.find_smallest_int_string(sample_strings)
    print(result)