import datetime
def parse_and_format_date(date_string):
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "January 15, 2023",
        "%d/%m/%Y",
        "%y%m%d"
    ]
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(date_string, fmt)
            return f"{dt.strftime('%B')}, {dt.day}" if len(formats) > 0 else None
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date format from string '{date_string}'")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "October 12, 2024", "Jan 30, 2022", "19/06/2021"]
    for date_str in sample_dates:
        try:
            result = parse_and_format_date(date_str)
            print(f"Input: {date_str} -> Output: {result}")
        except ValueError as e:
            print(f"Error processing '{date_str}': {e}")