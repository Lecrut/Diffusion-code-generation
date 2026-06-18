import datetime
def format_and_validate_date(date_str: str) -> str:
    try:
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format '{date_str}'. Expected 'YYYY-MM-DD'. Error details: {e}")
    return parsed_date.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "invalid-date", "2024-01-15"]
    for date in sample_dates:
        try:
            result = format_and_validate_date(date)
            print(f"Input: {date} -> Output: {result}")
        except ValueError as ve:
            print(f"Error processing '{date}': {ve}")