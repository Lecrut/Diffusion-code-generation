import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    if not isinstance(now, datetime.datetime):
        raise ValueError("Failed to get current date and time")
    
    day_of_week = now.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    try:
        print(get_current_day_of_week())
    except Exception as e:
        print(f"An error occurred: {e}")