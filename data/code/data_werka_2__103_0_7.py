import datetime
def get_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()
def format_elapsed_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
if __name__ == '__main__':
    total_seconds = get_seconds_since_midnight()
    formatted_time = format_elapsed_time(total_seconds)
    print(total_seconds)
    print(formatted_time)