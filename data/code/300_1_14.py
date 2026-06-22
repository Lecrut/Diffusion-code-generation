import calendar

class MonthDays:
    def __init__(self):
        self.months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, target_month: int, year: int) -> int:
        if target_month < 1 or target_month > 12:
            raise ValueError("Month must be between 1 and 12")
        
        if self.is_leap_year(year):
            self.months[2] = 29
        else:
            self.months[2] = 28

        return self.months[target_month]

if __name__ == '__main__':
    month_days = MonthDays()
    print(month_days.days_in_month(1, 2023))
    print(month_days.days_in_month(12, 2024))
    print(month_days.days_in_month(2, 2024))
    print(month_days.days_in_month(7, 2025))