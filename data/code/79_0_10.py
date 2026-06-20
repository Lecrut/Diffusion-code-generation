import datetime

def calculate_next_month(start_date):
    if not isinstance(start_date, datetime.date):
        raise ValueError("Invalid input: start_date must be an instance of datetime.date")
    
    year = start_date.year
    month = start_date.month
    
    try:
        next_date = start_date.replace(month=month + 1)
    except ValueError:
        if month == 2 and start_date.day > 28:
            next_date = start_date.replace(year=year + 1, month=1, day=28)
        else:
            raise ValueError("Invalid date provided")
    
    return next_date

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    try:
        next_month_date = calculate_next_month(sample_date)
        print(next_month_date)
    except ValueError as e:
        print(e)