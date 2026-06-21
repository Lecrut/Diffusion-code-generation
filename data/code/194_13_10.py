class StringAnalyzer:
    DEFAULT_ITEMS = ["apple", "banana", "cherry", "date"]

    @staticmethod
    def find_longest_item(items=DEFAULT_ITEMS):
        longest = items[0]
        for item in items:
            if len(item) > len(longest):
                longest = item
        return longest

if __name__ == '__main__':
    print(StringAnalyzer.find_longest_item())