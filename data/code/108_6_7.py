import sys
def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12."
    if not (1 <= day <= 31):
        return False, "Day must be between 1 and 31."
    if month in [4, 6, 9, 11]:
        if day > 30:
            return False, "Days in this month are at most 30."
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False, "February 29th is not valid for this year (non-leap year)."
            if day > 28:
                return False, "February has 28 days in a common year."
        else:
            if day > 28:
                return False, "February has 28 days in a common year."
    return True, day
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 31
    valid, result = validate_date(sample_year, sample_month, sample_day)
    if valid:
        print(result)
    else:
        print(f"Error: Invalid date input. Details: {result}")