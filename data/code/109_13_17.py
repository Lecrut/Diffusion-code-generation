import datetime

def days_left_in_month(start_date):
    if start_date.month == 12:
        end_date = start_date.replace(year=start_date.year + 1, month=1, day=1)
    else:
        end_date = start_date.replace(month=start_date.month + 1, day=1)
    
    return (end_date - start_date).days

if __name__ == '__main__':
    sample_date = datetime.date(2023, 9, 18)
    remaining_days = days_left_in_month(sample_date)
    print(remaining_days)