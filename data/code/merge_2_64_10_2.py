import datetime
def convert_date_to_full_month(date_str: str) -> str:
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.strftime('%B %d, %Y')}"
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.") from e
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-07-20",
        "2025-01-01"
    ]
    for date_str in sample_dates:
        try:
            result = convert_date_to_full_month(date_str)
            print(result)
        except ValueError as ve:
            print(f"Error processing {date_str}: {ve}")