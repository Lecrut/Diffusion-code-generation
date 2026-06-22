import datetime

class DateUtil:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_input):
        if isinstance(date_input, datetime.date):
            return date_input.weekday() in DateUtil.WEEKEND_DAYS
        elif isinstance(date_input, str):
            try:
                date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                return date_obj.weekday() in DateUtil.WEEKEND_DAYS
            except ValueError:
                return False
        else:
            return False
if __name__ == '__main__':
    dates_to_test = [datetime.date(2023, 10, 28), '2023-10-29', datetime.date(2023, 10, 30), '2023-10-31']
    for date in dates_to_test:
        print(f'{date}: {DateUtil.is_weekend(date)}')