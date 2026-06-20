import calendar
WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def determine_weekday(year, month, day):
    return WEEKDAY_NAMES[calendar.weekday(year, month, day)]
if __name__ == '__main__':
    print(determine_weekday(2023, 10, 26))
    print(determine_weekday(2023, 10, 27))