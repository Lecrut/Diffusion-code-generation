class ListAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest(self):
        if not self.numbers:
            raise ValueError("Input list cannot be empty")
        largest = self.numbers[0]
        for number in self.numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    analyzer = ListAnalyzer([3.14, 2.71, 1.618, 0.577, 1.414])
    print(analyzer.find_largest())