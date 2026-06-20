from datetime import datetime

def elapsed_time_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(elapsed_time_since_midnight())