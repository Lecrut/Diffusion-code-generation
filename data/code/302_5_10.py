class YearCalculator:
    def __init__(self, year):
        self.year = year
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_year(self):
        if self.is_leap:
            return 366
        else:
            return 365

if __name__ == '__main__':
    calculator_2023 = YearCalculator(2023)
    print(calculator_2023.days_in_year())

    calculator_2024 = YearCalculator(2024)
    print(calculator_2024.days_in_year())