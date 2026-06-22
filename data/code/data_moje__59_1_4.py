class DigitSummer:
    def __init__(self, value):
        self.value = value

    def calculate_sum(self):
        digits = map(int, str(abs(self.value)))
        return sum(digits)

    def get_formatted_result(self):
        return f"The sum is: {self.calculate_sum()}"

if __name__ == '__main__':
    target_number = 75392
    calculator = DigitSummer(target_number)
    print(calculator.calculate_sum())
    print(calculator.get_formatted_result())