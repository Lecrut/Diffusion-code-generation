import datetime

class DateChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_input):
        if isinstance(date_input, datetime.date):
            day_of_week = date_input.weekday()
        elif isinstance(date_input, str):
            try:
                date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                day_of_week = date_obj.weekday()
            except ValueError:
                return False
        else:
            return False
        return day_of_week in DateChecker.WEEKEND_DAYS
if __name__ == '__main__':
    checker = DateChecker()
    dates_to_test = [datetime.date(2023, 10, 28), '2023-10-29', datetime.date(2023, 10, 30), '2023-10-31']
    results = [checker.is_weekend(date) for date in dates_to_test]
    print(results)