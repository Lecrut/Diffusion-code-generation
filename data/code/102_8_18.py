import datetime

def is_weekday(iso_date):
    try:
        date_obj = datetime.datetime.fromisoformat(iso_date)
        return date_obj.weekday() < 5
    except ValueError as e:
        raise ValueError('Invalid ISO format date string') from e
if __name__ == '__main__':
    print(is_weekday('2023-10-25'))
    print(is_weekday('2023-10-28'))