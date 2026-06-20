import datetime
DAYS_PER_TIMDELTA = 1 / (24 * 60 * 60)

def calculate_day_difference(date1, date2):
    difference = date1 - date2
    return abs(difference.days + DAYS_PER_TIMDELTA * difference.seconds)
if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    print(calculate_day_difference(d1, d2))