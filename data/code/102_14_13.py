import calendar

def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return calendar.monthrange(year, month)[0] < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-05'))
    print(is_weekday('2023-10-06'))