import calendar

def determine_weekday(year, month, day):
    weekday_num = calendar.weekday(year, month, day)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[weekday_num]
if __name__ == '__main__':
    print(determine_weekday(2023, 10, 26))
    print(determine_weekday(2024, 2, 29))