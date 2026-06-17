from datetime import datetime, timedelta
def calculate_new_date(date_str: str, years: int) -> str:
    try:
        original_date = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = original_date + timedelta(days=years * 365.25)
        return new_date.strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError as e:
        raise ValueError(f"Invalid date format or calculation error: {e}")
if __name__ == '__main__':
    sample_date = "2023-10-05"
    years_to_add = 5
    result = calculate_new_date(sample_date, years_to_add)
    print(result)