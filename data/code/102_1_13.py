import calendar
dates_to_check = {'2023-10-23': 'Is weekday?', '2023-10-24': 'Is weekday?', '2023-10-28': 'Is not a weekday?', '2023-10-29': 'Is not a weekday?'}

def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return calendar.weekday(year, month, day) < 5
if __name__ == '__main__':
    for date, message in dates_to_check.items():
        print(f'{message} {date}: {is_weekday(date)}')