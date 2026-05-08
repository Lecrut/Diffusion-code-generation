import datetime
class DateCalculator:
    def get_next_date(self, start_date_str, days_to_add):
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        next_date = start_date + datetime.timedelta(days=days_to_add)
        return next_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    calculator = DateCalculator()
    start_date_str = "2023-10-26"
    days_to_add = 10
    next_date = calculator.get_next_date(start_date_str, days_to_add)
    print(next_date)