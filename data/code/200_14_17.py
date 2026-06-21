import itertools

class TupleSumCalculator:
    def __init__(self, tuples):
        self.tuples = tuples
    
    def calculate_sum(self):
        return sum(itertools.starmap(lambda _, value: value, self.tuples))

if __name__ == '__main__':
    sample_data = [
        (1, 10),
        (2, 20),
        (3, 30)
    ]
    calculator = TupleSumCalculator(sample_data)
    print(calculator.calculate_sum())