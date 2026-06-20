import calendar

class DateValidator:
    WEEKDAY_RANGE = range(0, 5)

    @staticmethod
    def is_weekday(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
            return date_obj.weekday() in DateValidator.WEEKDAY_RANGE
        except ValueError:
            return False

if __name__ == '__main__':
    validator = DateValidator()
    dates = ["01/01/2024", "02/29/2024", "03/15/2024", "12/31/2023", "04/30/2024", "13/01/2024"]
    for date in dates:
        print(f"Is {date} a weekday? {validator.is_weekday(date)}")