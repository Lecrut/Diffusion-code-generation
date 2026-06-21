from datetime import datetime

def calculate_year_difference(dt1: datetime, dt2: datetime) -> int:
    if dt1 > dt2:
        dt1, dt2 = dt2, dt1
    
    years = dt2.year - dt1.year
    
    if (dt2.month, dt2.day) < (dt1.month, dt1.day):
        years -= 1
        
    return abs(years)

if __name__ == '__main__':
    date1 = datetime(2020, 2, 29)
    date2 = datetime(2023, 2, 28)
    result = calculate_year_difference(date1, date2)
    print(result)