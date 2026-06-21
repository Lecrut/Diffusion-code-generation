class StringAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_longest_element(self):
        return max(self.data, key=len)

if __name__ == '__main__':
    analyzer = StringAnalyzer(["apple", "banana", "kiwi", "orange"])
    longest_item = analyzer.find_longest_element()
    print(longest_item)