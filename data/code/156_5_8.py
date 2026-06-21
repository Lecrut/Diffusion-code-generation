class AverageCalculator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if isinstance(number, (int, float)):
            self.numbers.append(number)

    def calculate_average(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        else:
            raise ValueError("No numbers to calculate average")

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_number(10)
    calculator.add_number(20)
    calculator.add_number(30)
    calculator.add_number(40)
    calculator.add_number(50)

    try:
        avg = calculator.calculate_average()
        print(f"The calculated average is: {avg}")
    except ValueError as e:
        print(e)