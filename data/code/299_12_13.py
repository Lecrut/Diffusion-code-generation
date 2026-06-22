class DateChecker:
    def is_weekend(self, date_input):
        try:
            import datetime
            date = datetime.datetime.strptime(str(date_input), '%Y-%m-%d').date()
            return date.weekday() >= 5
        except ValueError:
            return False

if __name__ == '__main__':
    checker = DateChecker()
    dates = ["2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-05"]
    for date in dates:
        print(f"{date} is weekend: {checker.is_weekend(date)}")