import datetime
def parse_date_to_full_month(date_str: str) -> str:
    supported_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "January 15, 2023",
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
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023"
    ]
    for date_input in sample_dates:
        result = parse_date_to_full_month(date_input)
        print(f"{date_input} -> {result}")