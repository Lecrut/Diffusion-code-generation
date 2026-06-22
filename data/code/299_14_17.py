import datetime

class DateChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
            return date_obj.weekday() in DateChecker.WEEKEND_DAYS
        except ValueError:
            raise ValueError('Invalid date format. Please enter the date in YYYY-MM-DD format.')
if __name__ == '__main__':
    checker = DateChecker()
    sample_dates = ['2023-10-27', '2023-10-28', '2024-01-01', '2024-01-07']
    for date in sample_dates:
        if checker.is_weekend(date):
            print(f'The date {date} is a weekend.')
        else:
            print(f'The date {date} is a weekday.')