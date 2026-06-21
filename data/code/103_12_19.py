from datetime import datetime, time

def get_elapsed_time():
    now = datetime.now()
    midnight = datetime.combine(now.date(), time.min)
    delta = now - midnight
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = get_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")