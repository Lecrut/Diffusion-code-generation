from datetime import date

class DateChecker:
    def is_weekend(self, date):
        weekday = date.weekday()
        return weekday >= 5

if __name__ == '__main__':
    checker = DateChecker()
    date1 = date(2023, 10, 6)
    date2 = date(2023, 10, 7)
    date3 = date(2023, 10, 8)
    print(f"Is {date1} a weekend? {checker.is_weekend(date1)}")
    print(f"Is {date2} a weekend? {checker.is_weekend(date2)}")
    print(f"Is {date3} a weekend? {checker.is_weekend(date3)}")