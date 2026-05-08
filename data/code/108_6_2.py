import sys
def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False, "All inputs must be integers."
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12."
    if not (1 <= day <= 31):
        return False, "Day must be between 1 and 31."
    if month == 2 and year % 4 == 0:
        if day > 29:
            return False, "February cannot have more than 29 days in a non-leap year."
    elif month == 2:
        if day > 28:
            return False, "February cannot have more than 28 days in a non-leap year."
    return True, day
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 31
    try:
        is_valid, result = validate_date(sample_year, sample_month, sample_day)
        if is_valid:
            print(result)
        else:
            print(f"Error: Invalid date combination for Year: {sample_year}, Month: {sample_month}, Day: {sample_day}. Details: {result}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")