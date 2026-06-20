from datetime import date, timedelta

def get_next_month_date(current_date):
    year = current_date.year
    month = current_date.month
    day = current_date.day
    
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    
    next_month_first_day = date(year, month, 1)
    
    return next_month_first_day

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(get_next_month_date(sample_date))