from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if date1 > date2:
        date1, date2 = date2, date1
    
    years = date2.year - date1.year
    
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1
        
    return years

if __name__ == '__main__':
    start_date = datetime(2000, 2, 29)
    end_date = datetime(2024, 2, 28)
    result = calculate_year_difference(start_date, end_date)
    print(result)