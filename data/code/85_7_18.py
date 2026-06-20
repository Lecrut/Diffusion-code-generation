from datetime import date, timedelta

def weeks_between_dates(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    print(weeks_between_dates(date(2023, 1, 1), date(2023, 1, 15)))  # Output: 2
    print(weeks_between_dates(date(2023, 1, 15), date(2023, 1, 1)))  # Output: 2