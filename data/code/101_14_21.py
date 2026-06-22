import calendar

def get_day_of_week(year, month, day):
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    result = get_day_of_week(2025, 3, 15)
    print(days[result])