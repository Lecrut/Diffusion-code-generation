import calendar

def get_weekday_name(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]
if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 26))
    print(get_weekday_name(2024, 1, 1))
    print(get_weekday_name(2025, 12, 31))