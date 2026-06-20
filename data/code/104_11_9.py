import datetime

def calculate_days_difference(date1, date2):
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise ValueError("Both inputs must be instances of datetime.datetime")
    
    return abs((date1 - date2).days)

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    print(calculate_days_difference(d1, d2))