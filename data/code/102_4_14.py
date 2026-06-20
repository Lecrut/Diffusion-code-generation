from datetime import datetime

def is_weekday(date_string: str) -> bool:
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return 0 <= date_obj.weekday() <= 4
    except ValueError:
        raise ValueError('Invalid Date Format')
if __name__ == '__main__':
    dates = ['2023-10-23', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-05']
    for date in dates:
        try:
            result = is_weekday(date)
            print(f'{date}: {('Weekday' if result else 'Weekend')}')
        except ValueError as e:
            print(e)