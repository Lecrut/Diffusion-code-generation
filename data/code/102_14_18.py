import datetime

class DateValidator:
    @staticmethod
    def is_weekday(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
            return date_obj.isoweekday() <= 5
        except ValueError:
            return False

if __name__ == '__main__':
    validator = DateValidator()
    print(f"Is 01/01/2024 a weekday? {validator.is_weekday('01/01/2024')}")
    print(f"Is 02/29/2024 a weekday? {validator.is_weekday('02/29/2024')}")
    print(f"Is 03/15/2024 a weekday? {validator.is_weekday('03/15/2024')}")