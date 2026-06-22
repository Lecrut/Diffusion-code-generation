from datetime import date, timedelta

def next_fifteenth_after(start_date):
    year = start_date.year
    month = start_date.month
    
    if month < 3:
        target_year = year
        target_month = 3
    elif month == 3:
        if start_date.day <= 15:
            target_year = year
            target_month = 3
        else:
            target_year = year
            target_month = 4
    else:
        target_year = year
        target_month = month + 1
        
    if target_month > 12:
        target_year += 1
        target_month = 1
        
    target_date = date(target_year, target_month, 15)
    return target_date

if __name__ == '__main__':
    start = date(2023, 3, 3)
    result = next_fifteenth_after(start)
    print(result)