class ListAnalyzer:
    def __init__(self, items):
        self.items = items

    def find_longest_item(self):
        if not self.items:
            return ""
        longest_string = self.items[0]
        for s in self.items:
            if len(s) > len(longest_string):
                longest_string = s
        return longest_string

if __name__ == '__main__':
    analyzer = ListAnalyzer(["apple", "banana", "kiwi", "strawberry", "grapefruit"])
    result = analyzer.find_longest_item()
    print(result)