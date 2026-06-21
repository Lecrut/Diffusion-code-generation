class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number):
        if isinstance(number, (int, float)):
            self.total += number
            self.count += 1
        else:
            raise ValueError("Invalid input. Please provide a valid number.")

    def calculate_average(self):
        if self.count > 0:
            return self.total / self.count
        else:
            raise ValueError("No numbers added to calculate the average.")

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    for number in sample_numbers:
        try:
            calculator.add_number(number)
        except ValueError as e:
            print(e)

    try:
        average = calculator.calculate_average()
        print(f"The calculated average is: {average}")
    except ValueError as e:
        print(e)