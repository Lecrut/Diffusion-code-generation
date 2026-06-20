from datetime import datetime, timedelta

def time_left_in_month():
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2023, 4, 30)
    today = datetime.now()
    
    if today < start_date or today > end_date:
        return "Date out of range"
    
    days_left = (end_date - today).days
    return f"{days_left} days left in the month"

if __name__ == '__main__':
    print(time_left_in_month())