import datetime

class DateChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            day_of_week = date_obj.weekday()
            return day_of_week in DateChecker.WEEKEND_DAYS
        except ValueError:
            raise ValueError('Invalid date format. Please enter the date in YYYY-MM-DD format.')
if __name__ == '__main__':
    sample_dates = ['2023-10-27', '2023-10-28', '2024-01-01', '2024-01-07']
    checker = DateChecker()
    for date in sample_dates:
        result = 'weekend' if checker.is_weekend(date) else 'weekday'
        print(f'The date {date} is a {result}.')