from datetime import date

def year_difference(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    
    years = end_date.year - start_date.year
    
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
        
    return years

if __name__ == '__main__':
    d1 = date(2020, 5, 15)
    d2 = date(2023, 5, 14)
    result = year_difference(d1, d2)
    print(result)