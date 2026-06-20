from datetime import date, timedelta

def remaining_time_in_month():
    start_date = date(2023, 4, 1)
    end_date = date(2023, 4, 30)
    today = date.today()
    
    if today < start_date:
        return timedelta(days=0)
    elif today > end_date:
        return timedelta(days=0)
    else:
        remaining_days = (end_date - today).days
        return timedelta(days=remaining_days)

if __name__ == '__main__':
    print(remaining_time_in_month())