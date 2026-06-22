class MaxValueCalculator:
    def __init__(self):
        self.data = [1.5, 3.2, 7.8, 2.4, 9.1, 4.6, 8.3]

    def compute_largest(self):
        if not self.data:
            raise ValueError("Data list is empty")
        largest = self.data[0]
        for value in self.data[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    calculator = MaxValueCalculator()
    result = calculator.compute_largest()
    print(result)