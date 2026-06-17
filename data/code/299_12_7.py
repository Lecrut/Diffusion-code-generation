class DateChecker:
    def is_weekend(self, date_input):
        try:
            import datetime
            date = datetime.datetime.strptime(str(date_input), "%Y-%m-%d").date()
            weekday = date.weekday()
            return weekday >= 5
        except ValueError:
            return False
if __name__ == '__main__':
    checker = DateChecker()
    print(f"Is 2023-10-28 a weekend? {checker.is_weekend('2023-10-28')}")
    print(f"Is 2023-10-29 a weekend? {checker.is_weekend('2023-10-29')}")
    print(f"Is 2023-10-30 a weekend? {checker.is_weekend('2023-10-30')}")
    print(f"Is 2023-10-31 a weekend? {checker.is_weekend('2023-10-31')}")
    print(f"Is 2023-11-05 a weekend? {checker.is_weekend('2023-11-05')}")
    print(f"Is 2023-11-06 a weekend? {checker.is_weekend('2023-11-06')}")
    print(f"Is invalid date '2023/10/28' a weekend? {checker.is_weekend('2023/10/28')}")