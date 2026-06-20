import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    print(is_weekday(sample_date))
    invalid_date = 'not a date'
    print(is_weekday(invalid_date))