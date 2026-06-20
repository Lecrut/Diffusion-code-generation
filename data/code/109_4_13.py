from datetime import date

def days_in_month(year, month):
    if month == 12:
        return 31
    else:
        return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]

def days_remaining(current_date):
    today = date.today()
    current_month = today.month
    current_year = today.year
    
    if current_date > today:
        return "Invalid date: future dates are not allowed"
    
    if current_month == today.month:
        return days_in_month(current_year, current_month) - current_date.day
    
    remaining_days = days_in_month(current_year, current_month) - current_date.day
    for month in range(current_month + 1, today.month):
        remaining_days += days_in_month(current_year, month)
    remaining_days += today.day
    
    return remaining_days

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    result = days_remaining(sample_date)
    print(result)