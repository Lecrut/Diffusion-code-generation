from datetime import date

def is_weekday(date_obj: date) -> bool:
    weekday = date_obj.weekday()
    return 0 <= weekday <= 4

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 2)
    sample_date2 = date(2023, 10, 6)
    
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")