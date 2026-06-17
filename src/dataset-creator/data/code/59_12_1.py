import datetime
def get_day_name(year: int) -> str:
    if year < 1000 or year > 9999:
        raise ValueError("Invalid year range. Year must be between 1 and 9999.")
    try:
        date_obj = datetime.date(year, 12, 31)
    except ValueError as e:
        if "day" in str(e):
            raise ValueError(f"Invalid day for the given year. Year {year} is not a leap year or has an invalid month/day combination.") from None
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_year = 2023
    try:
        result = get_day_name(sample_year)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")