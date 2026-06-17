import calendar
def get_day_of_month(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise TypeError("All inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Day is out of range for the given month and year")
    return day
if __name__ == '__main__':
    print(get_day_of_month(2023, 10, 5))
    try:
        print(get_day_of_month(2023, 10, 32))
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        print(get_day_of_month(2023, 13, 15))
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        print(get_day_of_month(2024, 2, 30))
    except ValueError as e:
        print(f"Error caught: {e}")