class StringAnalyzer:
    def __init__(self, items):
        self.items = items

    def find_longest_item(self):
        longest = self.items[0]
        for item in self.items:
            if len(item) > len(longest):
                longest = item
        return longest

if __name__ == '__main__':
    analyzer = StringAnalyzer(["apple", "banana", "cherry", "date"])
    print(analyzer.find_longest_item())