from datetime import datetime

def is_weekday(date_string: str) -> bool:
    dt = datetime.fromisoformat(date_string)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2023-10-23", "2023-10-24", "2023-10-28"]
    results = [is_weekday(d) for d in sample_dates]
    print(results)