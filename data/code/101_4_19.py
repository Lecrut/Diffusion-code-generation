from datetime import datetime

def get_day_of_week(date_string: str) -> int:
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.weekday()

if __name__ == '__main__':
    sample_dates = [
        "2023-10-23",
        "2024-01-01",
        "2000-02-29",
        "1999-12-31"
    ]
    for date_str in sample_dates:
        result = get_day_of_week(date_str)
        print(result)