import datetime
import time
def calculate_elapsed_time():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    elapsed_seconds = end_time - start_time
    total_seconds = int(elapsed_seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    print(calculate_elapsed_time())