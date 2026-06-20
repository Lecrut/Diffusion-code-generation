from datetime import date

def months_difference(date1: date, date2: date) -> int:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be date objects.")
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    
    return (year_diff * 12) + month_diff

if __name__ == '__main__':
    date1 = date(2023, 5, 15)
    date2 = date(2024, 3, 20)
    
    try:
        difference = months_difference(date1, date2)
        print(difference)
    except ValueError as e:
        print(e)