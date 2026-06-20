import datetime

def get_time_elapsed_since_midnight():
    current_time = datetime.datetime.now()
    midnight = datetime.datetime.combine(current_time.date(), datetime.time.min)
    
    if not isinstance(current_time, datetime.datetime) or not isinstance(midnight, datetime.datetime):
        raise ValueError("Failed to create date time objects.")
    
    time_difference = current_time - midnight
    return time_difference

if __name__ == '__main__':
    elapsed_time = get_time_elapsed_since_midnight()
    print(f"Time elapsed since midnight: {elapsed_time}")