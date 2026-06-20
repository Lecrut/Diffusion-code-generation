import time

def get_current_utc_timestamp():
    return int(time.time())

def calculate_seconds_since_midnight():
    current_utc = get_current_utc_timestamp()
    midnight_utc = (current_utc // 86400) * 86400
    seconds_since_midnight = current_utc - midnight_utc
    return seconds_since_midnight

if __name__ == '__main__':
    seconds = calculate_seconds_since_midnight()
    print(seconds)