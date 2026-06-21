import datetime

_UNITS = {
    "day": 86400,
    "hour": 3600,
    "minute": 60,
    "second": 1
}

def compute_seconds_since_midnight() -> float:
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    total_seconds = delta.total_seconds()
    days = int(total_seconds // _UNITS["day"])
    remaining = total_seconds - (days * _UNITS["day"])
    hours = int(remaining // _UNITS["hour"])
    remaining = remaining - (hours * _UNITS["hour"])
    minutes = int(remaining // _UNITS["minute"])
    seconds = remaining - (minutes * _UNITS["minute"])
    return days * _UNITS["day"] + hours * _UNITS["hour"] + minutes * _UNITS["minute"] + seconds

if __name__ == '__main__':
    result = compute_seconds_since_midnight()
    print(result)