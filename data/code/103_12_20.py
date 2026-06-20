from datetime import datetime

def calculate_elapsed_time():
    now = datetime(2023, 10, 5, 14, 30, 45)
    midnight = datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    hours = elapsed_time.seconds // 3600
    minutes = elapsed_time.seconds % 3600 // 60
    seconds = elapsed_time.seconds % 60
    return f'{hours} hours, {minutes} minutes, and {seconds} seconds'
if __name__ == '__main__':
    print(calculate_elapsed_time())