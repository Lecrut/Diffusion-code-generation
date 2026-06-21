import threading
import time

_lock = threading.Lock()

def get_elapsed_seconds_from_midnight():
    with _lock:
        now = time.time()
        start_of_day = now - (now % 86400)
        elapsed = now - start_of_day
        return elapsed

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)