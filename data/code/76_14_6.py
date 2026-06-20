from datetime import date

def days_between_dates(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of date.")
    
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 15)
    print(days_between_dates(date1, date2))