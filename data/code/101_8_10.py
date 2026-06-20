import calendar

def get_weekday_name(year, month, day):
    weekday_num = calendar.weekday(year, month, day)
    weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    return weekdays[weekday_num]
if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 26))
    print(get_weekday_name(2023, 10, 27))