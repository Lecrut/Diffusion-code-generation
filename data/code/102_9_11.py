import datetime

def is_weekday(date_obj):
    return date_obj.weekday() < 5

def check_dates():
    date_mapping = {
        '20231027': datetime.date(2023, 10, 27),
        '20231028': datetime.date(2023, 10, 28),
        '20231029': datetime.date(2023, 10, 29),
        '20231030': datetime.date(2023, 10, 30)
    }
    
    results = {date: is_weekday(date_mapping[date]) for date in date_mapping}
    
    for date, result in results.items():
        print(f"Is {date} a weekday? {result}")

if __name__ == '__main__':
    check_dates()