class StringAnalyzer:
    @staticmethod
    def find_longest_string(string_list):
        if not string_list:
            return None
        longest_string = ""
        for s in string_list:
            if len(s) > len(longest_string):
                longest_string = s
        return longest_string
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringAnalyzer.find_longest_string(sample_list)
    print(result)