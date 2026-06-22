from datetime import date
import datetime

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or isinstance(first, datetime.datetime):
        raise ValueError("First argument must be a date object")
    if not isinstance(second, date) or isinstance(second, datetime.datetime):
        raise ValueError("Second argument must be a date object")
    
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    date_a = date(2024, 1, 1)
    date_b = date(2023, 12, 31)
    comparison_result = compare_dates(date_a, date_b)
    print(comparison_result)