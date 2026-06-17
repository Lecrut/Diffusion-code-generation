import calendar
def get_day_of_month(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("All inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Day is out of range for the given month")
    return day
if __name__ == '__main__':
    print(get_day_of_month(2023, 10, 5))
    print(get_day_of_month(2024, 1, 1))
    print(get_day_of_month(2023, 12, 31))
    try:
        get_day_of_month(2023, 13, 1)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month(2023, 10, 32)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month(2023, 10, -5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month(2023, "October", 5)
    except TypeError as e:
        print(f"Error caught: {e}")