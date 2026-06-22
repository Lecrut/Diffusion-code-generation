from datetime import datetime, timedelta

def days_remaining(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    first_day_of_next_month = datetime(next_year, next_month, 1)
    last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
    
    today = datetime.now()
    days_diff = (last_day_of_current_month - today).days
    
    return max(0, days_diff)

if __name__ == '__main__':
    year1 = 2023
    month1 = 5
    print(f"Days remaining in {year1}-{month1}: {days_remaining(year1, month1)}")
    
    year2 = 2024
    month2 = 8
    print(f"Days remaining in {year2}-{month2}: {days_remaining(year2, month2)}")