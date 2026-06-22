def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise TypeError("Input must be a string")
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    if year < 1 or month < 1 or month > 12 or day < 1:
        raise ValueError("Invalid date values")
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    if day > days_in_month[month]:
        raise ValueError("Invalid day for month")
    if month <= 2:
        year -= 1
        month += 12
    j = year // 100
    k = year % 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return h not in (0, 6)

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = is_weekday(sample_date)
    print(result)