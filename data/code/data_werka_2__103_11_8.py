import time
import datetime

def compute_seconds_since_midnight() -> float:
    now = time.time()
    start_of_day = now - (now % 86400)
    return now - start_of_day

if __name__ == '__main__':
    result = compute_seconds_since_midnight()
    print(result)