import datetime
def get_day_name(year: int, month: int, day: int) -> str:
    if year < 1000 or year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date components. {e}") from None
    return str(date_obj.strftime("%A"))
if __name__ == '__main__':
    print(get_day_name(2023, 10, 5))