from datetime import datetime

def months_between_dates(date1, date2):
    if not (isinstance(date1, datetime) and isinstance(date2, datetime)):
        raise ValueError("Both inputs must be datetime objects.")
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    
    return year_diff * 12 + month_diff

if __name__ == '__main__':
    try:
        date1 = datetime(2020, 5, 15)
        date2 = datetime(2023, 8, 20)
        print(months_between_dates(date1, date2))
    except ValueError as e:
        print(e)