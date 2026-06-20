class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month):
        days_in_month = [0, 31, 28 if not self.is_leap(self.year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[month]

    def calculate_day_of_year(self):
        cumulative_days = sum(self.days_in_month(m) for m in range(1, self.month))
        cumulative_days += self.day
        return cumulative_days

if __name__ == '__main__':
    calculator = DateCalculator(2023, 10, 26)
    print(calculator.calculate_day_of_year())
    
    calculator = DateCalculator(2024, 1, 1)
    print(calculator.calculate_day_of_year())
    
    calculator = DateCalculator(2000, 2, 29)
    print(calculator.calculate_day_of_year())
    
    calculator = DateCalculator(2023, 12, 31)
    print(calculator.calculate_day_of_year())
    
    calculator = DateCalculator(2023, 1, 1)
    print(calculator.calculate_day_of_year())
    
    calculator = DateCalculator(2023, 3, 1)
    print(calculator.calculate_day_of_year())