from datetime import date

def is_weekday(date_obj: date) -> bool:
    weekday = date_obj.weekday()
    return 0 <= weekday < 5

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 2),
        date(2023, 10, 3),
        date(2023, 10, 6),
        date(2023, 10, 7)
    ]
    
    for sample_date in sample_dates:
        print(f"Is {sample_date} a weekday? {is_weekday(sample_date)}")