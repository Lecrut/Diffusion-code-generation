from datetime import datetime

def is_weekday(date_string: str) -> bool:
    dt = datetime.fromisoformat(date_string)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_dates = [
        "2023-10-23",
        "2023-10-28",
        "2023-10-29",
        "2023-10-30",
        "2023-10-31",
        "2023-11-01",
    ]
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)