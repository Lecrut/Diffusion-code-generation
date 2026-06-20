from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be of type 'date'")
    
    delta = abs((date2 - date1).days)
    return delta // 365

if __name__ == '__main__':
    d1 = date(2010, 1, 1)
    d2 = date(2023, 4, 15)
    print(years_between_dates(d1, d2))