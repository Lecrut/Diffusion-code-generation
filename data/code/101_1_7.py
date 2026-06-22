import calendar

def get_weekday_name(year: int, month: int, day: int) -> str:
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    result = get_weekday_name(2023, 10, 5)
    print(result)