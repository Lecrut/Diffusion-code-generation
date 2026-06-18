import datetime
def get_day_of_week(year: int, month: int, day: int) -> str:
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except ValueError:
        raise ValueError(f"Invalid date {year}-{month}-{day}")
if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 5))