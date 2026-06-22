from datetime import datetime
import calendar

def is_weekday(date_string: str) -> bool:
    dt = datetime.fromisoformat(date_string)
    return dt.weekday() < 5

if __name__ == '__main__':
    test_dates = ["2024-02-05", "2024-02-10"]
    for d in test_dates:
        print(is_weekday(d))