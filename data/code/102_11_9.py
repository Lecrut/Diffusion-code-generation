def is_weekday(date_string: str) -> bool:
    if len(date_string) != 10:
        raise ValueError("Invalid date format")
    if date_string[4] != '-' or date_string[7] != '-':
        raise ValueError("Invalid date format")
    try:
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
    except ValueError:
        raise ValueError("Invalid date components")
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1:
        raise ValueError("Invalid day")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    if day > days_in_month[month]:
        raise ValueError("Invalid day for month")
    if year < 1:
        raise ValueError("Year must be positive")
    days_from_0001 = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    for m in range(1, month):
        days_from_0001 += days_in_month[m]
    days_from_0001 += day
    weekday = days_from_0001 % 7
    return weekday < 5

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)