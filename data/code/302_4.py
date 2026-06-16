import datetime
def get_day_of_month(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("All inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.day
    except ValueError as e:
        raise ValueError(f"Invalid date combination: {e}")
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