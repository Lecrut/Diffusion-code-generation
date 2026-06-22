class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, num):
        if isinstance(num, (int, float)):
            self.total += num
            self.count += 1
        else:
            print(f"Skipping invalid input: {num}")

    def calculate_average(self):
        if self.count > 0:
            return self.total / self.count
        else:
            print("No valid numbers were entered.")
            return None

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_number(10)
    calculator.add_number(20)
    calculator.add_number('a')
    calculator.add_number(30)
    average = calculator.calculate_average()
    if average is not None:
        print(f"The average of the entered numbers is: {average}")