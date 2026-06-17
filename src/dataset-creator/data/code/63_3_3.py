import datetime
def calculate_future_date(date_str: str, years: int) -> str:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj.replace(year=date_obj.year + years)
        return new_date.isoformat()
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.") from e
if __name__ == '__main__':
    sample_date_str = "2023-10-05"
    sample_years = 5
    result = calculate_future_date(sample_date_str, sample_years)
    print(result)