class StringFinder:
    def find_longest_string(self, string_list):
        if not string_list:
            return None
        return max(string_list, key=len)

if __name__ == '__main__':
    finder = StringFinder()
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = finder.find_longest_string(sample_strings)
    print(result)