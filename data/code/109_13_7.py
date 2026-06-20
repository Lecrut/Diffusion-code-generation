from datetime import date, timedelta

def time_left_in_month(start_date='2023-04-01', end_date='2023-04-30'):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    today = date.today()
    
    if today < start or today > end:
        return "Date out of range"
    
    days_left = (end - today).days
    return days_left

if __name__ == '__main__':
    print(time_left_in_month())