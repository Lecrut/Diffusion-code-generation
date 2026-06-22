import datetime

def is_weekday(date_string):
    if not isinstance(date_string, str):
        raise TypeError("Expected string input")
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Date must be in YYYY-MM-DD format")
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        raise ValueError("Date components must have correct length")
    try:
        year_val = int(parts[0])
        month_val = int(parts[1])
        day_val = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    date_obj = datetime.date(year_val, month_val, day_val)
    return date_obj.weekday() < 5

if __name__ == "__main__":
    test_cases = [
        ("2023-10-06", "Friday"),
        ("2023-10-07", "Saturday"),
        ("2023-02-28", "Tuesday"),
        ("2024-02-29", "Thursday"),
        ("invalid", "Error"),
        ("2023-13-01", "Error")
    ]
    for case, label in test_cases:
        try:
            result = is_weekday(case)
            day_name = datetime.date.fromisoformat(case).strftime("%A") if label != "Error" else case
            print(f"is_weekday('{case}') = {result}")
        except (ValueError, TypeError) as e:
            print(f"is_weekday('{case}') raised {type(e).__name__}")