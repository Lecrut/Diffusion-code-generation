class MaxPairComparator:
    def __init__(self, numbers):
        self.numbers = numbers

    def compare_pairs(self):
        return [max(a, b) for a, b in zip(self.numbers, self.numbers[1:])]

if __name__ == '__main__':
    comparator = MaxPairComparator([3, 1, 4, 1, 5, 9, 2, 6])
    print(comparator.compare_pairs())