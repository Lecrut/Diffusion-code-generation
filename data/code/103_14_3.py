from datetime import datetime, timedelta

def get_elapsed_time_today():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - start_of_day
    total_seconds = int(elapsed.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(get_elapsed_time_today())