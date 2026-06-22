class RepeatedCharFinder:
    def __init__(self, text):
        self.text = text
        self.seen = set()
        self.repeated = set()

    def find(self):
        for char in self.text:
            if char in self.seen:
                self.repeated.add(char)
            else:
                self.seen.add(char)
        return list(self.repeated)

    def get_counts(self):
        counts = {}
        for char in self.text:
            if char in self.repeated:
                counts[char] = counts.get(char, 0) + 1
        return counts

if __name__ == '__main__':
    finder = RepeatedCharFinder("banana")
    print(finder.find())
    print(finder.get_counts())