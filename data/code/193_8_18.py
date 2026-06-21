class SumCalculator:
    def sum_elements(self, iterable):
        total = 0
        for item in iterable:
            total += item
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    large_dataset = range(1, 1000001)
    result = calculator.sum_elements(large_dataset)
    print(f"Sum of elements: {result}")