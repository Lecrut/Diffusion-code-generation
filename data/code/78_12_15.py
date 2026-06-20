from datetime import date

def months_between_dates(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of date.")
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    
    return (year_diff * 12) + month_diff

if __name__ == '__main__':
    try:
        date1 = date(2020, 1, 15)
        date2 = date(2023, 4, 10)
        print(months_between_dates(date1, date2))
    except ValueError as e:
        print(e)