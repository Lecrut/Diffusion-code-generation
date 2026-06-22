class AdjacentPairComparator:
    def __init__(self, numbers):
        self.numbers = numbers

    def compare_adjacent(self):
        result = []
        n = len(self.numbers)
        if n < 2:
            return result
        for i in range(n - 1):
            result.append(self.numbers[i] < self.numbers[i + 1])
        return result

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    comparator = AdjacentPairComparator(sample_array)
    print(comparator.compare_adjacent())