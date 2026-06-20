class MeanCalculator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Number must be an integer or a float")
        self.numbers.append(number)

    def calculate_mean(self):
        if not self.numbers:
            raise ValueError("The list of numbers cannot be empty.")
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    calculator.add_number(3.5)
    calculator.add_number(2.1)
    calculator.add_number(4.8)
    calculator.add_number(6.7)
    print(calculator.calculate_mean())