def is_valid_date(date_str):
    if len(date_str) != 10:
        return False
    parts = date_str.split('-')
    if len(parts) != 3:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    year, month, day = map(int, parts)
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month == 2 and day > 29:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    return True

def compare_dates(date_str1, date_str2):
    if not is_valid_date(date_str1) or not is_valid_date(date_str2):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))

    if (year1, month1, day1) > (year2, month2, day2):
        return 1
    elif (year1, month1, day1) < (year2, month2, day2):
        return -1
    else:
        return 0

if __name__ == '__main__':
    result = compare_dates("2023-10-26", "2023-10-25")
    print(result)