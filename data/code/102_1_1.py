import calendar

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) < 5
if __name__ == '__main__':
    print(is_weekday(2023, 10, 5))
    print(is_weekday(2023, 10, 6))