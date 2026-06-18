import datetime
def parse_date_to_full_month(date_str: str) -> str:
    supported_formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "January 15, 2023",
        "Feb-14-2023",
    ]
    for fmt in supported_formats:
        try:
            parsed_date = datetime.datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%B")
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "October 12, 2023",
        "14/09/2023",
        "Sep-28-2023",
        "Invalid Date"
    ]
    for date in sample_dates:
        try:
            result = parse_date_to_full_month(date)
            print(f"{date} -> {result}")
        except ValueError as e:
            print(f"{date} -> Error: {e}")