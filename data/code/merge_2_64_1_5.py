import datetime as dt
def normalize_date(date_input):
    if isinstance(date_input, str):
        try:
            parsed = dt.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            return None
    elif isinstance(date_input, (dt.date, dt.datetime)):
        parsed = date_input
    else:
        return None
    formatted_date = parsed.strftime("%B %d, %Y").title()
    if not isinstance(formatted_date, str):
        return None
    return f"{formatted_date}"
if __name__ == '__main__':
    sample_strings = ["2023-10-05", "2024-01-15"]
    sample_objects = [dt.date(2023, 9, 20), dt.datetime(2024, 6, 7)]
    results_str = []
    for s in sample_strings:
        result = normalize_date(s)
        if result is not None:
            results_str.append(result)
    results_obj = []
    for o in sample_objects:
        result = normalize_date(o)
        if result is not None:
            results_obj.append(result)
    print("String inputs:")
    for r in results_str:
        print(r)
    print("\nObject inputs:")
    for r in results_obj:
        print(r)