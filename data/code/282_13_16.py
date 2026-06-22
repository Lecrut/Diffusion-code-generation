class SumCalculator:
    def __init__(self):
        self.memo = {}

    def total_recursive_memoization(self, seq):
        if not seq:
            return 0
        if len(seq) in self.memo:
            return self.memo[len(seq)]
        result = seq[0] + self.total_recursive_memoization(seq[1:])
        self.memo[len(seq)] = result
        return result

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculator.total_recursive_memoization(sample_sequence))