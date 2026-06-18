import datetime
def parse_date_to_full_month(date_str):
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "January 15, 2023",
        "%d/%m/%Y",
        "%m/%d/%Y"
    ]
    for fmt in formats:
        try:
            parsed_date = datetime.datetime.strptime(date_str, fmt)
            return f"{parsed_date.strftime('%B')}"
        except ValueError:
            continue
    raise ValueError(f"No valid date format found for input: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "October 12, 2024",
        "15/06/2023",
        "June 28, 2022"
    ]
    for date_input in sample_dates:
        result = parse_date_to_full_month(date_input)
        print(f"{date_input} -> {result}")