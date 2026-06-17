import datetime
def parse_and_get_weekday(date_string: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%x",
        "%X",
        "dd.mm.yyyy",
        "yyyy-mm-dd"
    ]
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(date_string.strip(), fmt)
            return dt.strftime("%A")
        except ValueError:
            continue
    raise ValueError(f"No recognized date format found for input: {date_string}")
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "10.05.2023",
        "2023-10-05"
    ]
    for case in test_cases:
        try:
            result = parse_and_get_weekday(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"{case} -> Error: {e}")