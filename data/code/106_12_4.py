from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of date")
    
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    d1 = date(1980, 5, 15)
    d2 = date(2023, 4, 1)
    print(years_between_dates(d1, d2))