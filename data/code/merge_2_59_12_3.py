import datetime
def get_day_name(year: int, month: int, day: int) -> str:
    if year < 1 or year > 9999:
        raise ValueError("Year must be between 1 and 9999.")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date components. {e}") from None
    return str(date_obj.strftime("%A"))
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    try:
        day_name = get_day_name(sample_year, sample_month, sample_day)
        print(f"The full English name of the day is {day_name}.")
    except ValueError as ve:
        print(f"Error: {ve}")