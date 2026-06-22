class PatternYielder:
    def __init__(self):
        self.pattern = '123'
        self.index = 0

    def yield_pattern(self, k):
        for _ in range(k):
            yield self.pattern[self.index]
            self.index = (self.index + 1) % len(self.pattern)

if __name__ == '__main__':
    yielder = PatternYielder()
    result = list(yielder.yield_pattern(12))
    print(result)