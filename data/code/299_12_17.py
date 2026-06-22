import datetime

class DateChecker:
    def __init__(self):
        self.weekend_days = {5: "Saturday", 6: "Sunday"}

    def is_weekend(self, date_input):
        try:
            date = datetime.datetime.strptime(str(date_input), '%Y-%m-%d').date()
            weekday = date.weekday()
            return weekday in self.weekend_days
        except ValueError:
            return False

if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = ["2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-05"]
    for date in dates_to_check:
        print(f"{date} is weekend: {checker.is_weekend(date)}")