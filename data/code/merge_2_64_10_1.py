import datetime
def convert_date_to_full_month_name(date_str):
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.strftime('%B')} {dt.year}"
    except ValueError as e:
        raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD.") from e
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-07-20",
        "2025-01-01"
    ]
    for date_str in sample_dates:
        try:
            result = convert_date_to_full_month_name(date_str)
            print(f"{date_str} -> {result}")
        except ValueError as ve:
            print(f"Error processing '{date_str}': {ve}")