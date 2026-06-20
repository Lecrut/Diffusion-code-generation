import calendar

def get_weekday_name(year, month, day):
    weekday_number = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_number]

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 5))