class MonthDays:
    def __init__(self):
        self.days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days_in_month(self, year, month):
        if not 1 <= year <= 9999 or not 1 <= month <= 12:
            raise ValueError('Year must be between 1 and 9999, and month must be between 1 and 12')
        if month == 2:
            return self.days_per_month[month - 1] + int(self.is_leap_year(year))
        return self.days_per_month[month - 1]

if __name__ == '__main__':
    md = MonthDays()
    print(md.days_in_month(2023, 2))
    print(md.days_in_month(2024, 2))
    print(md.days_in_month(2023, 4))