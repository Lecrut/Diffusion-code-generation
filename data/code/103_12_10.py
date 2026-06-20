from datetime import datetime

def calculate_elapsed_time():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    hours = elapsed_time.seconds // 3600
    minutes = (elapsed_time.seconds // 60) % 60
    seconds = elapsed_time.seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = calculate_elapsed_time()
    print(f"Elapsed time today: {hours} hours, {minutes} minutes, {seconds} seconds")