import datetime
def normalize_date(date_input):
    if isinstance(date_input, str):
        try:
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return None
    elif isinstance(date_input, datetime.date) or isinstance(date_input, datetime.datetime):
        parsed = date_input
    else:
        return None
    formatted_date = parsed.strftime("%B %d, %Y").title()
    if not isinstance(formatted_date, str):
        return None
    return f"{formatted_date}"
if __name__ == '__main__':
    sample_strings = ["2023-10-05", "2024-07-20"]
    sample_objects = [datetime.date(2023, 9, 1), datetime.datetime(2024, 8, 15)]
    results = []
    for item in sample_strings:
        result = normalize_date(item)
        if isinstance(result, str):
            print(f"String '{item}' -> {result}")
        obj_item = [datetime.date(2023, 9, 1), datetime.datetime(2024, 8, 15)]
    for item in sample_objects:
        result = normalize_date(item)
        if isinstance(result, str):
            print(f"Object {item} -> {result}")