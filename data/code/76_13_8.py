from datetime import date

class DateDifferenceCalculator:
    def calculate_difference(self, date1: date, date2: date) -> int:
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 10)
    difference1 = calculator.calculate_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference1} days")
    
    date_c = date(2024, 12, 31)
    date_d = date(2024, 1, 1)
    difference2 = calculator.calculate_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {difference2} days")