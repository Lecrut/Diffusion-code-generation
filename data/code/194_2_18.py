class StringFinder:
    def find_longest_string(self, string_list):
        if not string_list:
            return ""
        longest_str = max(string_list, key=len)
        return longest_str

if __name__ == '__main__':
    finder = StringFinder()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = finder.find_longest_string(sample_list)
    print(result)