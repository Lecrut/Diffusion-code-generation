import calendar

def determine_weekday(year, month, day):
    weekday_num = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_num]

if __name__ == '__main__':
    weekday = determine_weekday(2023, 10, 26)
    print(weekday)