class DateCalculator:
    def calculate_month_diff(self, month1: int, month2: int) -> int:
        if not (1 <= month1 <= 12 and 1 <= month2 <= 12):
            raise ValueError("Month values must be between 1 and 12")
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(5, 10))