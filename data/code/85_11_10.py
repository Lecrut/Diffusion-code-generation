import datetime

def calculate_week_difference(date1: datetime.date, date2: datetime.date) -> int:
    return abs((date2 - date1).days // 7)

if __name__ == '__main__':
    sample_dates = [
        (datetime.date(2023, 1, 1), datetime.date(2023, 1, 8)),
        (datetime.date(2023, 1, 1), datetime.date(2023, 1, 7)),
        (datetime.date(2023, 1, 1), datetime.date(2023, 1, 1))
    ]
    
    for date1, date2 in sample_dates:
        result = calculate_week_difference(date1, date2)
        print(result)