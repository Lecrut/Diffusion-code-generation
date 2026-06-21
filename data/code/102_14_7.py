import calendar

def is_date_weekday(year, month, day):
    try:
        return calendar.isleap(year) or calendar.weekday(year, month, day) < 5
    except ValueError:
        return False

if __name__ == '__main__':
    print(is_date_weekday(2023, 10, 23))
    print(is_date_weekday(2023, 10, 28))