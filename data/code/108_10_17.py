import datetime
DATE_FORMAT = '%Y-%m-%d'

def get_day_of_week(year=2024, month=1, day=1):
    date_obj = datetime.datetime(year, month, day)
    return date_obj.strftime('%A')
if __name__ == '__main__':
    test_date = (2024, 1, 1)
    print(f'January 1st, {test_date[0]} falls on a {get_day_of_week(*test_date)}')