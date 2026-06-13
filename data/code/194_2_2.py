class ListAnalyzer:
    def get_longest_item(self, string_list):
        if not string_list:
            return ""
        longest_item = ""
        max_length = -1
        for item in string_list:
            if len(item) > max_length:
                max_length = len(item)
                longest_item = item
        return longest_item
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = analyzer.get_longest_item(sample_list)
    print(result)