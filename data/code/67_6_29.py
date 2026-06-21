class SumCalculator:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    def compute_sum(self):
        return self.attribute1 + self.attribute2

if __name__ == '__main__':
    initial_value1 = 4
    initial_value2 = 9
    sum_calculator = SumCalculator(initial_value1, initial_value2)
    result_sum = sum_calculator.compute_sum()
    print(result_sum)