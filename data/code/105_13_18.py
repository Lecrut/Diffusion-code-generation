import datetime

class DateFinder:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def find_next_weekend_date():
        today = datetime.date.today()
        days_to_add = (7 - today.weekday()) % 7
        next_weekend_date = today + datetime.timedelta(days=days_to_add)
        return next_weekend_date
if __name__ == '__main__':
    result = DateFinder.find_next_weekend_date()
    print(f'Next Weekend Date: {result}')