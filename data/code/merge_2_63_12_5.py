from datetime import datetime
def calculate_future_date(iso_string: str, year_diff: int) -> str:
    try:
        current_datetime = datetime.fromisoformat(iso_string)
        new_year = current_datetime.year + year_diff
        month = current_datetime.month
        day = min(current_datetime.day, 28 if len(str(month)) == 1 else 30 or (current_datetime.day <= 29 and is_leap(year)))
    except ValueError:
        raise ValueError("Invalid ISO format date provided.") from None
    return f"{new_year}-{month:02d}-{day:02d}"
def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_date = "2023-05-15"
    diff_years = 5
    result = calculate_future_date(sample_date, diff_years)
    print(result)