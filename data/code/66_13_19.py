class AdjacentElementChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_strictly_increasing_pairs(self):
        indices = []
        for i in range(len(self.numbers) - 1):
            if self.numbers[i] < self.numbers[i + 1]:
                indices.append(i)
        return indices

if __name__ == '__main__':
    sample_numbers = [5, 3, 8, 6, 9, 10, 2]
    checker = AdjacentElementChecker(sample_numbers)
    result = checker.find_strictly_increasing_pairs()
    print(result)