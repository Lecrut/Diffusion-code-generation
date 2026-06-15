class ListAnalyzer:
    def get_longest_item(self, string_list):
        if not string_list:
            return ""
        longest_string = ""
        for s in string_list:
            if len(s) > len(longest_string):
                longest_string = s
        return longest_string
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = analyzer.get_longest_item(sample_list)
    print(result)