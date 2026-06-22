class LengthCollector:
    def __init__(self):
        self.lengths = set()

    def add_string(self, string):
        self.lengths.add(len(string))

    def get_sorted_lengths(self):
        return sorted(self.lengths)

if __name__ == '__main__':
    collector = LengthCollector()
    for s in {"apple", "banana", "cherry", "date"}:
        collector.add_string(s)
    print(collector.get_sorted_lengths())