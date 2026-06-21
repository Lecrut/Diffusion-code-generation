def calculate_average(numbers):
    total = sum(x for x in numbers)
    count = len(numbers)
    return total / count if count > 0 else 0

class SampleCalculator:
    def __init__(self, sample):
        self.sample = sample
    
    def get_sample(self):
        return self.sample
    
    def calculate_average(self):
        return sum(x for x in self.sample) / len(self.sample)

if __name__ == '__main__':
    calculator = SampleCalculator([50, 60, 70])
    print(calculator.get_sample())
    print(calculator.calculate_average())