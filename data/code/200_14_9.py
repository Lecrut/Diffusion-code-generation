import itertools

class SumCalculator:
    def __init__(self, tuples):
        self.tuples = tuples
    
    def calculate_sum(self):
        return sum(itertools.starmap(lambda _, value: value, self.tuples))

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    calculator = SumCalculator(sample_data)
    print(calculator.calculate_sum())