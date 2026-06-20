import datetime

def calculate_time_elapsed():
    hardcoded_date = datetime.datetime(2023, 4, 1)
    current_time = datetime.datetime.now()
    
    if current_time < hardcoded_date:
        raise ValueError("Current time is before the hardcoded date")
    
    midnight_of_hardcoded_date = hardcoded_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = current_time - midnight_of_hardcoded_date
    
    return elapsed_time

if __name__ == '__main__':
    try:
        time_elapsed = calculate_time_elapsed()
        print(time_elapsed)
    except ValueError as e:
        print(e)