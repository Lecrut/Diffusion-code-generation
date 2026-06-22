import datetime

def calculate_elapsed_time_since_start_of_day(target_date):
    start_of_day = datetime.datetime.combine(target_date, datetime.time.min)
    end_of_day = datetime.datetime.combine(target_date, datetime.time.max)
    now = datetime.datetime.now()
    
    if now.date() != target_date:
        raise ValueError("The current date does not match the target date.")
        
    elapsed = now - start_of_day
    return elapsed

if __name__ == '__main__':
    today = datetime.date.today()
    result = calculate_elapsed_time_since_start_of_day(today)
    print(result)