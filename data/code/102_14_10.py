import calendar

def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    sample_dates = ['2023-10-23', '2023-10-21', '2023-10-22']
    for d in sample_dates:
        print(is_weekday(d))