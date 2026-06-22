from datetime import datetime, timedelta

def get_elapsed_time_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - midnight
    total_seconds = int(elapsed.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = get_elapsed_time_since_midnight()
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")