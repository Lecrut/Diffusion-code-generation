import time
from datetime import datetime

def get_elapsed_since_midnight():
    now = time.time()
    today_start = now - (now % 86400)
    elapsed = now - today_start
    units = {
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    result = []
    for unit_name, unit_value in units.items():
        if unit_name == 'seconds':
            val = int(elapsed % unit_value)
        elif unit_name == 'minutes':
            val = int((elapsed // unit_value) % 60)
        else:
            val = int(elapsed // unit_value)
        result.append(val)
    return tuple(result)

if __name__ == '__main__':
    h, m, s = get_elapsed_since_midnight()
    print(f"{h}:{m}:{s}")