from datetime import datetime, time

TIME_UNITS = {
    "hours": 3600,
    "minutes": 60,
    "seconds": 1
}

def get_current_time_string():
    now = datetime.now()
    midnight = datetime.combine(now.date(), time.min)
    delta = now - midnight
    total_seconds = int(delta.total_seconds())
    
    hours = total_seconds // TIME_UNITS["hours"]
    remaining = total_seconds % TIME_UNITS["hours"]
    minutes = remaining // TIME_UNITS["minutes"]
    seconds = remaining % TIME_UNITS["minutes"]
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(get_current_time_string())