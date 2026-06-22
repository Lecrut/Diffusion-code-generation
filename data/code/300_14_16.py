class MonthDays:
    def __init__(self):
        self.months = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

    def days_in_month(self, year, month):
        if month == 2:
            if self.is_leap_year(year):
                return 29
            else:
                return 28
        return self.months[month]

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    calculator = MonthDays()
    print(f"Days in February 2023: {calculator.days_in_month(2023, 2)}")
    print(f"Days in February 2024: {calculator.days_in_month(2024, 2)}")
    print(f"Days in April 2023: {calculator.days_in_month(2023, 4)}")