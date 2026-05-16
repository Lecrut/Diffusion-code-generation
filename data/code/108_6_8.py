import sys
def validate_date():
    year = 2023
    month = 10
    day = 25
    if not (1 <= month <= 12):
        print("Error: Invalid month. Month must be between 1 and 12.")
        return False
    if not (1 <= day <= 31):
        print("Error: Invalid day. Day must be between 1 and 31.")
        return False
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            max_day = 29
        else:
            max_day = 28
        if day > max_day:
            print(f"Error: Invalid day for the given month and year. February {year} only has {max_day} days.")
            return False
    elif month in [4, 6, 9, 11]:
        max_day = 30
        if day > max_day:
            print(f"Error: Invalid day. Month {month} only has {max_day} days.")
            return False
    else:
        max_day = 31
        if day > max_day:
            print(f"Error: Invalid day. Month {month} only has {max_day} days.")
            return False
    print(f"Validated Day of the Month: {day}")
    return True
if __name__ == '__main__':
    validate_date()