import datetime
def parse_date_to_weekday(date_string: str) -> tuple[str, bool]:
    supported_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%y-%m-%d",
        "%d.%m.%Y",
        "January 15, 2023"
    ]
    for fmt in supported_formats:
        try:
            parsed_date = datetime.datetime.strptime(date_string, fmt)
            weekday_name = parsed_date.strftime("%A")
            return (weekday_name, True)
        except ValueError:
            continue
    return ("Unknown", False)
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "23-10-05",
        "05.10.2023"
    ]
    for date_str in test_cases:
        result = parse_date_to_weekday(date_str)
        print(f"{date_str} -> {result[0]} (Valid: {result[1]})")