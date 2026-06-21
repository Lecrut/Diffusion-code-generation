from datetime import date, timedelta

def next_fifteenth_after(start_date: date) -> date:
    year = start_date.year
    month = start_date.month
    
    if month < 3:
        target_month = 3
        target_year = year
    elif month == 3:
        if start_date.day <= 15:
            target_month = 3
            target_year = year
        else:
            target_month = 4
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
    result = next_fifteenth_after(start)
    print(result)