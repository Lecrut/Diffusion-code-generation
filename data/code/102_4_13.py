from datetime import datetime

WEEKDAY_RANGE = (0, 4)

def is_weekday(date_string: str) -> bool:
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        weekday = date_obj.weekday()
        return WEEKDAY_RANGE[0] <= weekday <= WEEKDAY_RANGE[1]
    except ValueError:
        raise ValueError('Invalid Date Format')

if __name__ == '__main__':
    dates = [
        '2023-10-23',
        '2023-10-28',
        '2023-10-29',
        '2023-10-30',
        '2023-10-31',
        '2023-11-01'
    ]

    for date in dates:
        print(f'{date}: {is_weekday(date)}')