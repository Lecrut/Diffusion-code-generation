import datetime

def is_weekday(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2024-01-01", "2024-01-02", "2024-01-03"]
    results = {d: is_weekday(d) for d in sample_dates}
    print(results)