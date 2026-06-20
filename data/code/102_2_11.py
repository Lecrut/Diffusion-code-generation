from datetime import date

def is_weekday(date_obj: date) -> bool:
    weekday = date_obj.weekday()
    return 0 <= weekday < 5

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 2),
        date(2023, 10, 3),
        date(2023, 10, 4),
        date(2023, 10, 5),
        date(2023, 10, 6)
    ]
    results = {date_obj: is_weekday(date_obj) for date_obj in sample_dates}
    for date_obj, result in results.items():
        print(f"Is {date_obj} a weekday? {result}")