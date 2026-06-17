import datetime
def get_day_of_month(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("All inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    try:
        date = datetime.date(year, month, day)
        return date.day
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
        get_day_of_month(2023, 5, 32)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_day_of_month(2023, 2, 30)
    except ValueError as e:
        print(f"Error caught: {e}")