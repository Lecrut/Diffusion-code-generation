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
    year = parsed.year
    month_name = parsed.strftime("%B").capitalize()
    day = str(parsed.day).zfill(2) if len(str(parsed.day)) == 1 else str(parsed.day)
    return f"{year}-{month_name}-{day}"
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        datetime.date(2024, 6, 1),
        "2020-08-17"
    ]
    for date in sample_dates:
        print(normalize_date(date))