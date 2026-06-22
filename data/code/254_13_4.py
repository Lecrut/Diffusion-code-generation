class StringSearcher:
    def __init__(self, strings):
        self.strings = strings

    def find_shortest_string(self):
        if not self.strings:
            return None
        shortest = self.strings[0]
        for string in self.strings[1:]:
            if len(string) < len(shortest):
                shortest = string
        return shortest

if __name__ == '__main__':
    searcher = StringSearcher(["apple", "banana", "cherry", "date"])
    print(searcher.find_shortest_string())