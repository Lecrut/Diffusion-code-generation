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
    formatted_date = parsed.strftime("%B %d, %Y").title()
    if not isinstance(formatted_date, str):
        return None
    return f"{formatted_date}"
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        datetime.date(2024, 7, 1),
        datetime.datetime.now(),
        "invalid-date"
    ]
    for date in sample_dates:
        result = normalize_date(date)
        print(result if result else None)