import datetime

def days_until_end_of_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    
    target_date = datetime.date(year, month, 1)
    next_month_start = datetime.date(*next_month)
    days_in_month = (next_month_start - target_date).days
    days_remaining = days_in_month - (target_date.day - 1)
    
    return days_remaining

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    
    result = days_until_end_of_month(sample_year, sample_month)
    print(f"Days left until the end of {sample_month}/{sample_year}: {result}")