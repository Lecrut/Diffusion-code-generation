class PatternYielder:
    def __init__(self):
        self.pattern = '123'
    
    def yield_pattern(self, k):
        index = 0
        while k > 0:
            yield self.pattern[index]
            index = (index + 1) % len(self.pattern)
            k -= 1

if __name__ == '__main__':
    yielder = PatternYielder()
    sample_count = 8
    result = list(yielder.yield_pattern(sample_count))
    print(result)