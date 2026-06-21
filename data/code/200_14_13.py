import itertools

class TupleSumCalculator:
    def __init__(self, tuples):
        self.tuples = tuples
    
    def calculate_sum(self):
        return sum(itertools.starmap(lambda _, y: y, self.tuples))

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6)]
    calculator = TupleSumCalculator(sample_data)
    print(calculator.calculate_sum())