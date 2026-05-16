import sys
def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12."
    if not (1 <= day <= 31):
        return False, "Day must be between 1 and 31."
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False, "February cannot have 29 days in this year."
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False, f"Month {month} cannot have more than 30 days."
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False, f"Month {month} cannot have more than 31 days."
    return True, day
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 13
    sample_day = 32
    year = sample_year
    month = sample_month
    day = sample_day
    is_valid, result = validate_date(year, month, day)
    if is_valid:
        print(result)
    else:
        print(f"Error: Invalid date input. {result}")