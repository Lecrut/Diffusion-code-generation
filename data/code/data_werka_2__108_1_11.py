def get_day_of_month(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a number')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    seconds_per_day = 86400
    days_since_epoch = int(timestamp // seconds_per_day)
    year = 1970
    month = 1
    day = 1

    def is_leap_year(y):
        return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

    def days_in_month(y, m):
        if m in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif m in (4, 6, 9, 11):
            return 30
        elif m == 2:
            return 29 if is_leap_year(y) else 28
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days_since_epoch < days_in_year:
            break
        days_since_epoch -= days_in_year
        year += 1
    while True:
        dim = days_in_month(year, month)
        if days_since_epoch < dim:
            break
        days_since_epoch -= dim
        month += 1
    day = days_since_epoch + 1
    return day
if __name__ == '__main__':
    timestamp = 1697328000
    result = get_day_of_month(timestamp)
    print(result)
    timestamp2 = 0
    result2 = get_day_of_month(timestamp2)
    print(result2)