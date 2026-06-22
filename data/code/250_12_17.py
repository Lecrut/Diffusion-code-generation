class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, num):
        if isinstance(num, (int, float)):
            self.total += num
            self.count += 1
        else:
            print(f"Error: '{num}' is not a valid number. Skipping.")

    def calculate_average(self):
        if self.count > 0:
            return self.total / self.count
        else:
            return None

if __name__ == '__main__':
    calculator = AverageCalculator()
    numbers = [10, 20, '30', 40, 50]
    for num in numbers:
        calculator.add_number(num)
    
    average = calculator.calculate_average()
    if average is not None:
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No valid numbers were entered to calculate the average.")