from datetime import datetime

def is_weekday(date_string: str) -> bool:
    parsed_date = datetime.fromisoformat(date_string)
    return parsed_date.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2023-10-07", "2023-10-08"]
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)