from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    years = end_date.year - start_date.year
    
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    
    return abs(years)

if __name__ == '__main__':
    date1 = datetime(2020, 2, 29)
    date2 = datetime(2023, 2, 28)
    result = calculate_year_difference(date1, date2)
    print(result)