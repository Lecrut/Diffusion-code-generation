import datetime
def parse_date_to_weekday(date_str: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "dd/mm/yyyy",
        "%b%d%Y",
        "yyyy-mm-dd"
    ]
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(date_str, fmt)
            return dt.strftime("%A")
        except ValueError:
            continue
    raise ValueError(f"No date format matched the input string: {date_str}")
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "October 05, 2023",
        "05/10/2023",
        "Oct052023",
        "2023-10-05"
    ]
    for case in test_cases:
        try:
            result = parse_date_to_weekday(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"Error parsing '{case}': {e}")