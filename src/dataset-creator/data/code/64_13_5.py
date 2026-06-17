import datetime
from dateutil.parser import parse as date_parse
def format_date_with_full_month(date_str):
    try:
        dt = date_parse(date_str)
        return dt.strftime("%B %d, %Y")
    except Exception:
        raise ValueError(f"Unable to parse date string: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "01/15/2023",
        "January 15th, 2023",
        "15-Jan-2023",
        "Feb. 28, 2024",
        "March 1st, 2025"
    ]
    for date_str in sample_dates:
        try:
            result = format_date_with_full_month(date_str)
            print(result)
        except ValueError as e:
            print(f"Error processing {date_str}: {e}")