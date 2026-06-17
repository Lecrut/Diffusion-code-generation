from datetime import date
class DateChecker:
    def is_weekend(self, date):
        day_of_week = date.weekday()
        return day_of_week >= 5
if __name__ == '__main__':
    checker = DateChecker()
    date1 = date(2023, 10, 21)
    print(f"Is {date1} a weekend? {checker.is_weekend(date1)}")
    date2 = date(2023, 10, 22)
    print(f"Is {date2} a weekend? {checker.is_weekend(date2)}")
    date3 = date(2023, 10, 28)
    print(f"Is {date3} a weekend? {checker.is_weekend(date3)}")
    date4 = date(2023, 10, 29)
    print(f"Is {date4} a weekend? {checker.is_weekend(date4)}")