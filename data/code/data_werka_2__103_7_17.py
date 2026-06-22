from datetime import datetime, timedelta

def get_elapsed_time_from_day_start():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    total_seconds = int(delta.total_seconds())
    units = {
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    remaining = total_seconds
    hours = remaining // units['hours']
    remaining %= units['hours']
    minutes = remaining // units['minutes']
    remaining %= units['minutes']
    seconds = remaining // units['seconds']
    return {
        'total_seconds': total_seconds,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'raw_delta': delta
    }

if __name__ == '__main__':
    result = get_elapsed_time_from_day_start()
    print(result)