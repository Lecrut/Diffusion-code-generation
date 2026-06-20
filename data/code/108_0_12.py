import datetime

def get_day_of_month(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.day
    except ValueError as e:
        print(f'Invalid date: {e}')
        return None
if __name__ == '__main__':
    test_dates = [(2023, 10, 26), (2024, 10, 25), (2023, 2, 29), (2023, 13, 1)]
    for year, month, day in test_dates:
        print(f'Day of the month for {year}-{month}-{day}: {get_day_of_month(year, month, day)}')