import datetime
def parse_date_to_weekday(date_string: str) -> tuple[str, bool]:
    supported_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d.%m.%Y",
        "%Y%m%d",
    ]
    for fmt in supported_formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, fmt)
            weekday_name = date_obj.strftime("%A")
            return (weekday_name, True)
        except ValueError:
            continue
    return ("Unknown format or invalid date", False)
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "Oct 05, 2023",
        "05 October 2023",
        "05.10.2023",
        "20231005"
    ]
    for date_str in sample_dates:
        weekday, is_valid = parse_date_to_weekday(date_str)
        print(f"{date_str} -> {weekday}, Validated: {is_valid}")