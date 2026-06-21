from functools import reduce

def calculate_total_and_count(data):
    return reduce(lambda acc, x: (acc[0] + x, acc[1] + 1), data, (0, 0))

class AverageCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_average(self):
        total, count = calculate_total_and_count(self.data)
        if count == 0:
            return 0
        return total / count

if __name__ == '__main__':
    calculator1 = AverageCalculator([2, 4, 6, 8, 10])
    print(f"Average of dataset: {calculator1.calculate_average()}")