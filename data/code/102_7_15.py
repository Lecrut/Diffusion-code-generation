import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError as e:
        print(f'Error: {e}')
        return False
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 4)
    result = is_weekday(sample_date)
    print(result)