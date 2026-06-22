class PatternYielder:
    PATTERN = '123'

    @staticmethod
    def yield_pattern(k):
        index = 0
        while k > 0:
            yield PatternYielder.PATTERN[index]
            index = (index + 1) % len(PatternYielder.PATTERN)
            k -= 1

if __name__ == '__main__':
    sample_count = 8
    result = list(PatternYielder.yield_pattern(sample_count))
    print(result)