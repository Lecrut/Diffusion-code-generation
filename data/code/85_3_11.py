import datetime

def calculate_weeks_between_julian_dates(julian_date1: int, julian_date2: int) -> float:
    date1 = datetime.datetime(2000, 1, 1) + datetime.timedelta(days=julian_date1 - 1)
    date2 = datetime.datetime(2000, 1, 1) + datetime.timedelta(days=julian_date2 - 1)
    difference = abs(date1 - date2)
    weeks = difference.days / 7
    return weeks
if __name__ == '__main__':
    julian_date1 = 366
    julian_date2 = 394
    result = calculate_weeks_between_julian_dates(julian_date1, julian_date2)
    print(f'Difference in weeks: {result:.2f}')