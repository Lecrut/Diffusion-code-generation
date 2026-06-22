class StringComparer:
    def __init__(self, strings):
        self.strings = strings

    def get_later_strings(self):
        return [max(pair) for pair in zip(self.strings, self.strings[1:])]

if __name__ == '__main__':
    comparer = StringComparer(["apple", "banana", "cherry", "date"])
    result = comparer.get_later_strings()
    print(result)