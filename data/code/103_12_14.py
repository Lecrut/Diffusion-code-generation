from datetime import datetime

def elapsed_time():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    delta = now - midnight
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(elapsed_time())