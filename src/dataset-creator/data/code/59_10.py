import datetime
def calculate_day_of_week(year: int, month: int, day: int) -> str:
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}. Error details: {e}")
if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 5),
        (2024, 2, 29),
        (2021, 6, 7)
    ]
    for year, month, day in sample_dates:
        result = calculate_day_of_week(year, month, day)
        print(f"{year}-{month}-{day} is a {result}")