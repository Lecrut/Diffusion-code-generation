class SumCalculator:
    def __init__(self, data):
        self._data = list(data)
    
    def calculate_sum(self):
        return sum(self._data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    calculator = SumCalculator(sample_list)
    result = calculator.calculate_sum()
    print(result)