class IndexExtractor:
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def extract(self, idx):
        if not isinstance(idx, int):
            raise ValueError("Index must be an integer")
        if idx < 0 or idx >= len(self.primary) or idx >= len(self.secondary):
            raise ValueError("Index out of range")
        return [(self.primary[idx], self.secondary[idx])]

if __name__ == '__main__':
    p = [10, 20, 30]
    s = [40, 50, 60]
    extractor = IndexExtractor(p, s)
    print(extractor.extract(1))
    print(extractor.extract(0))