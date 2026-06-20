from datetime import datetime

def calculate_elapsed_time():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - midnight
    hours = elapsed.seconds // 3600
    minutes = (elapsed.seconds // 60) % 60
    seconds = elapsed.seconds % 60
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(calculate_elapsed_time())