from dateutil.relativedelta import relativedelta

def calculate_remaining_days(year, month):
    from datetime import date
    if not (1 <= year <= 9999) or not (1 <= month <= 12):
        raise ValueError("Invalid input: Year must be between 1 and 9999, month must be between 1 and 12")
    
    current_date = date(year, month, 1)
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    remaining_days = (next_month - current_date).days
    return remaining_days

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    result1 = calculate_remaining_days(year1, month1)
    print(f"Remaining days in {year1}-{month1:02d}: {result1}")