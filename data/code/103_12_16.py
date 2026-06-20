from datetime import datetime

def calculate_elapsed_time():
    current_time = datetime(2023, 10, 5, 14, 30, 45)
    midnight = datetime(current_time.year, current_time.month, current_time.day)
    elapsed_time = current_time - midnight
    hours = elapsed_time.seconds // 3600
    minutes = (elapsed_time.seconds % 3600) // 60
    seconds = elapsed_time.seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = calculate_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")