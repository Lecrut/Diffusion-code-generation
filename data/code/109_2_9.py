from datetime import datetime, timedelta

def remaining_time_in_month():
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2023, 4, 30)
    today = datetime.now()
    
    if today < start_date:
        return timedelta(days=0)
    elif today > end_date:
        return timedelta(days=0)
    else:
        return end_date - today

if __name__ == '__main__':
    print(remaining_time_in_month())