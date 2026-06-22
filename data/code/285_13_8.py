class StringComparator:
    def __init__(self, strings):
        self.strings = strings

    def compare_adjacent(self):
        return [max(pair) for pair in zip(self.strings, self.strings[1:])]

if __name__ == '__main__':
    comparator = StringComparator(["apple", "banana", "cherry", "date"])
    result = comparator.compare_adjacent()
    print(result)