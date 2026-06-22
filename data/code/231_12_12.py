class PatternGenerator:
    PATTERN = '123'

    @staticmethod
    def yield_pattern(k):
        index = 0
        while k > 0:
            yield PatternGenerator.PATTERN[index]
            index = (index + 1) % len(PatternGenerator.PATTERN)
            k -= 1

if __name__ == '__main__':
    sample_count = 12
    result = list(PatternGenerator.yield_pattern(sample_count))
    print(result)