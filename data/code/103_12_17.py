from datetime import datetime

def get_time_elapsed_today():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = now - start_of_day
    return elapsed_time.seconds // 3600, (elapsed_time.seconds % 3600) // 60, elapsed_time.seconds % 60

if __name__ == '__main__':
    hours, minutes, seconds = get_time_elapsed_today()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")