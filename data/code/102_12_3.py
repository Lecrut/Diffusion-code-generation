class DateChecker:
    def check_weekday(self, date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
            weekday = date_obj.weekday()
            return 0 <= weekday <= 6
        except ValueError:
            return False
if __name__ == '__main__':
    import datetime
    checker = DateChecker()
    date1 = "2023-10-25"
    date2 = "2023-10-26"
    date3 = "2023-10-27"
    date4 = "2023-10-28"
    date5 = "2023-10-29"
    invalid_date = "2023/10/30"
    print(f"Is {date1} a weekday? {checker.check_weekday(date1)}")
    print(f"Is {date2} a weekday? {checker.check_weekday(date2)}")
    print(f"Is {date3} a weekday? {checker.check_weekday(date3)}")
    print(f"Is {date4} a weekday? {checker.check_weekday(date4)}")
    print(f"Is {date5} a weekday? {checker.check_weekday(date5)}")
    print(f"Is {invalid_date} a weekday? {checker.check_weekday(invalid_date)}")