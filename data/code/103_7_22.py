import datetime
import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
HOURS_IN_DAY = 24

UNIT_LABELS = {
    'hours': 0,
    'minutes': 1,
    'seconds': 2
}

FORMAT_ORDER = ['hours', 'minutes', 'seconds']

def get_time_since_midnight():
    current = datetime.datetime.now()
    midnight = datetime.datetime.min.replace(year=current.year, month=current.month, day=current.day)
    delta = current - midnight
    total_secs = int(delta.total_seconds())
    
    h = total_secs // SECONDS_IN_HOUR
    rem = total_secs % SECONDS_IN_HOUR
    m = rem // SECONDS_IN_MINUTE
    s = rem % SECONDS_IN_MINUTE
    
    values = [h, m, s]
    labels = ['hours', 'minutes', 'seconds']
    
    parts = []
    for val, label in zip(values, labels):
        if val > 0 or parts:
            parts.append(f"{val}")
    
    if not parts:
        parts = ["0"]
        
    return ", ".join(f"{val} {label}" for val, label in zip(parts, labels))

if __name__ == '__main__':
    result = get_time_since_midnight()
    print(result)