import datetime

def days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start_year = 2023
    start_month = 1
    start_day = 1
    end_year = 2023
    end_month = 12
    end_day = 31
    
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    
    print(f"Days between {start_date} and {end_date}: {days_between(start_date, end_date)}")