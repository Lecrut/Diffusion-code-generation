from datetime import datetime, timedelta

def remaining_time_in_month():
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2023, 4, 30)
    current_date = datetime.now()
    
    if current_date >= end_date:
        return timedelta(days=0)
    
    remaining_days = (end_date - current_date).days
    return timedelta(days=remaining_days)

if __name__ == '__main__':
    print(remaining_time_in_month())