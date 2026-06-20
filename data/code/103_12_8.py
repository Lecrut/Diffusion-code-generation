from datetime import datetime

def calculate_elapsed_time():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed = now - midnight
    hours = elapsed.seconds // 3600
    minutes = (elapsed.seconds % 3600) // 60
    seconds = elapsed.seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = calculate_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")