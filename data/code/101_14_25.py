import datetime
import calendar

def get_day_of_week(year: int, month: int, day: int) -> str:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    max_days = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_days):
        raise ValueError(f"Day must be between 1 and {max_days}")
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2025, 3, 15)
    print(result)