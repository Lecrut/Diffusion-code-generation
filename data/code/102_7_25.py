import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError:
        print('Invalid date object provided')
        return False

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 7)
    print(is_weekday(sample_date))
    invalid_input = 'not a date'
    print(is_weekday(invalid_input))