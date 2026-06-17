class DateChecker:
    def is_weekend(self, date_input):
        try:
            import datetime
            date_obj = datetime.datetime.strptime(str(date_input), '%Y-%m-%d').date()
            weekday = date_obj.weekday()
            return weekday >= 5
        except ValueError:
            return False
if __name__ == '__main__':
    checker = DateChecker()
    date1 = "2023-10-28"
    date2 = "2023-10-29"
    date3 = "2023-10-30"
    date4 = "2023-10-31"
    date5 = "2023-11-05"
    print(f"{date1} is weekend: {checker.is_weekend(date1)}")
    print(f"{date2} is weekend: {checker.is_weekend(date2)}")
    print(f"{date3} is weekend: {checker.is_weekend(date3)}")
    print(f"{date4} is weekend: {checker.is_weekend(date4)}")
    print(f"{date5} is weekend: {checker.is_weekend(date5)}")
    invalid_date = "2023/10/28"
    print(f"{invalid_date} is weekend: {checker.is_weekend(invalid_date)}")