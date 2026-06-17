import datetime
def parse_and_get_weekday(date_string: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "dd/mm/yyyy",
        "%d/%m/%Y",
        "%b %d, %Y",
        "%M/%d/%y",
        "%d-%b-%Y"
    ]
    for fmt in formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, fmt)
            return date_obj.strftime("%A")
        except ValueError:
            continue
    raise ValueError(f"No recognized format found for input: {date_string}")
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "October 05, 2023",
        "05/10/2023",
        "05/10/23",
        "Oct 05, 2023",
        "10/05/23",
        "05-Oct-2023"
    ]
    for case in test_cases:
        result = parse_and_get_weekday(case)
        print(f"{case} -> {result}")