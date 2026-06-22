from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if date1 > date2:
        date1, date2 = date2, date1
    
    years = date2.year - date1.year
    
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1
        
    return abs(years)

if __name__ == '__main__':
    d1 = datetime(2020, 2, 29)
    d2 = datetime(2023, 3, 1)
    result = calculate_year_difference(d1, d2)
    print(result)