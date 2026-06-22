import calendar

def is_date_weekday(year: int, month: int, day: int) -> bool:
    return calendar.isleap(year) or calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    result = is_date_weekday(2023, 10, 23)
    print(result)