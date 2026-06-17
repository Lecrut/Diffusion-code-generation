import datetime
def parse_and_get_weekday(date_string: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%x",
        "%X"
    ]
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(date_string, fmt)
            return dt.strftime("%A")
        except ValueError:
            continue
    raise ValueError(f"No recognized format found for date string: {date_string}")
if __name__ == '__main__':
    test_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023"
    ]
    for date_str in test_dates:
        weekday = parse_and_get_weekday(date_str)
        print(f"{date_str} -> {weekday}")