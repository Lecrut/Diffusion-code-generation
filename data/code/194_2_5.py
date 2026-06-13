class ListAnalyzer:
    def get_longest_item(self, string_list):
        if not string_list:
            return ""
        longest_string = ""
        for item in string_list:
            if len(item) > len(longest_string):
                longest_string = item
        return longest_string
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = analyzer.get_longest_item(sample_list)
    print(result)