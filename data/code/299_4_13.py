import datetime

class DateChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
            return date_obj.weekday() in DateChecker.WEEKEND_DAYS
        except ValueError:
            return False
if __name__ == '__main__':
    dates_to_check = ['01/01/2024', '01/06/2024', '03/15/2024', '12/25/2023', '02/17/2024']
    checker = DateChecker()
    for date in dates_to_check:
        print(f'{date}: {checker.is_weekend(date)}')