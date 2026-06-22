import datetime

def get_seconds_elapsed_since_midnight():
    now = datetime.datetime.now()
    today = now.date()
    tomorrow = today + datetime.timedelta(days=1)
    midnight = datetime.datetime.combine(tomorrow, datetime.time.min)
    diff = midnight - now
    seconds = diff.total_seconds()
    return seconds

if __name__ == '__main__':
    result = get_seconds_elapsed_since_midnight()
    print(result)