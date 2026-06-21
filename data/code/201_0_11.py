def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_numbers(self):
        return self.numbers
    
    def set_numbers(self, new_numbers):
        self.numbers = new_numbers
    
    def calculate_average(self):
        if not self.numbers:
            return None
        total = sum(self.numbers)
        count = len(self.numbers)
        mean = total / count
        return mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator(sample_values)
    print("Original numbers:", calculator.get_numbers())
    new_values = [15, 25, 35, 45, 55]
    calculator.set_numbers(new_values)
    print("Updated numbers:", calculator.get_numbers())
    print("Average of updated numbers:", calculator.calculate_average())