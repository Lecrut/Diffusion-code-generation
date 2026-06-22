class StringFinder:
    def __init__(self, strings):
        self.strings = strings

    def find_shortest_string(self):
        if not self.strings:
            return None
        shortest = self.strings[0]
        for string in self.strings:
            if len(string) < len(shortest):
                shortest = string
        return shortest

if __name__ == '__main__':
    finder = StringFinder(["apple", "banana", "cherry", "date"])
    print(finder.find_shortest_string())