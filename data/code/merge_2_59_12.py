import datetime
def get_day_name(year: int, month: int, day: int) -> str:
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date input. Error details: {e}") from None
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_index = date_obj.weekday() + 1 if year >= datetime.MINYEAR and month in range(1, 13) else None
    return days_of_week[day_index - 1]
if __name__ == '__main__':
    sample_year = 2024
    sample_month = 5
    sample_day = 18
    result_date_name = get_day_name(sample_year, sample_month, sample_day)
    print(result_date_name)