import calendar

def determine_weekday(year, month, day):
    try:
        weekday_num = calendar.weekday(year, month, day)
        return calendar.day_name[weekday_num]
    except ValueError:
        raise ValueError('Invalid date provided')
if __name__ == '__main__':
    print(determine_weekday(2023, 10, 26))