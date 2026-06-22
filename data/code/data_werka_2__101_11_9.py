import datetime

def get_day_of_week(year: int, month: int, day: int) -> str:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {e}")
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)