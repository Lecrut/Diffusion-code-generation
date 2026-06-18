import datetime
def normalize_date(date_input):
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return None
    elif isinstance(date_input, (datetime.date, datetime.datetime)):
        parsed = date_input
    else:
        return None
    year = int(parsed.year)
    month_name = parsed.strftime("%B").capitalize()
    day = str(parsed.day).zfill(2)
    return f"{month_name} {day}, {year}"
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        datetime.date(2024, 7, 1),
        "2020-03-12T14:30:00"
    ]
    for case in test_cases:
        result = normalize_date(case)
        print(result)