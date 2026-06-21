import datetime

def get_day_of_week(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2024, 2, 29)
    print(result)