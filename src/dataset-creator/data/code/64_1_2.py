import datetime
def normalize_date(date_input):
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return None
    elif isinstance(date_input, datetime.datetime):
        parsed = date_input.date()
    else:
        return None
    year = parsed.year
    month_name = parsed.strftime("%B").capitalize()
    if len(month_name) > 2 and not month_name[0].isupper():
        first_char = month_name[0]
        rest = month_name[1:]
        capitalization = f"{first_char.upper()}{rest}"
        return f"{capitalization} {year}"
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        datetime.datetime(2024, 7, 1),
        "2020-12-31"
    ]
    for date in sample_dates:
        result = normalize_date(date)
        print(result)