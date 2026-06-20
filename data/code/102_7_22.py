import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError:
        print('Error: Provided object does not have a weekday method.')
        return None
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5)
    print(is_weekday(sample_date))
    sample_date = datetime.date(2023, 10, 6)
    print(is_weekday(sample_date))