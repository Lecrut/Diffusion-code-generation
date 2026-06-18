import datetime as dt
def parse_date_to_weekday(date_str):
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "dd-mm-yyyy",
        "%B %d, %Y",
        "%d %b %Y"
    ]
    for fmt in formats:
        try:
            parsed_date = dt.datetime.strptime(date_str, fmt)
            return str(parsed_date.strftime("%A"))
        except ValueError:
            continue
    raise ValueError(f"No matching date format found for input: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "10/05/2023",
        "05-10-2023",
        "October 5, 2023",
        "5 Oct 2023"
    ]
    for date_str in sample_dates:
        try:
            result = parse_date_to_weekday(date_str)
            print(f"{date_str} -> {result}")
        except ValueError as e:
            print(f"Error parsing '{date_str}': {e}")