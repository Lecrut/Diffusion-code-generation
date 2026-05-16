import sys
def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12."
    if not (1 <= day <= 31):
        return False, "Day must be between 1 and 31."
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