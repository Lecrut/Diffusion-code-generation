def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def timestamp_to_month(timestamp):
    year = timestamp // (31536000 + int(is_leap_year(timestamp // 31536000))) + 1970
    day = (timestamp % 31536000) // 86400
    month = 1
    while day >= days_in_month(year, month):
        day -= days_in_month(year, month)
        month += 1
    return year * 12 + month

def calculate_month_diff(timestamp1, timestamp2):
    if timestamp1 > timestamp2:
        timestamp1, timestamp2 = timestamp2, timestamp1
    month1 = timestamp_to_month(timestamp1)
    month2 = timestamp_to_month(timestamp2)
    return abs(month2 - month1)

if __name__ == '__main__':
    print(calculate_month_diff(1633075200, 1645196800))