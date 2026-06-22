import datetime

def get_elapsed_time_since_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time(0, 0, 0))
    delta = now - midnight
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    result = get_elapsed_time_since_midnight()
    print(result)