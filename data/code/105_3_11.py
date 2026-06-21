from datetime import date, timedelta

def next_15th_after(start_date):
    year = start_date.year
    month = start_date.month
    
    if start_date.day <= 15:
        target_month = month
        target_year = year
    else:
        target_month = month + 1
        target_year = year
        
    if target_month > 12:
        target_month = 1
        target_year += 1
        
    return date(target_year, target_month, 15)

if __name__ == '__main__':
    start = date(2023, 3, 3)
    result = next_15th_after(start)
    print(result)