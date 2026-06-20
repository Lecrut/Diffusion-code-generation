import datetime

def days_between_dates(start_date, end_date):
    delta = end_date - start_date
    return abs(delta.days)

if __name__ == '__main__':
    start_year = 2023
    start_month = 1
    start_day = 1
    end_year = 2023
    end_month = 12
    end_day = 31
    
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    
    days_diff = days_between_dates(start_date, end_date)
    print(f"Days between January 1, 2023 and December 31, 2023: {days_diff}")