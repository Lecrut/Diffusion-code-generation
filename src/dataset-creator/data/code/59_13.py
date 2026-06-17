from datetime import datetime
def get_weekday(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.weekday()
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "2024-06-18",
        "2025-01-01"
    ]
    for date in test_cases:
        print(f"{date} -> {get_weekday(date)}")