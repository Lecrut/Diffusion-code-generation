import datetime
def get_day_of_week(year: int, month: int, day: int) -> str:
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date {year}-{month}-{day}: {e}")
if __name__ == '__main__':
    year = 2023
    month = 10
    day = 5
    result_day_of_week = get_day_of_week(year, month, day)
    print(f"{year}-{month:02d}-{day:02d} is a {result_day_of_week}")