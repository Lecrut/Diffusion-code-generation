import datetime
import time
def calculate_elapsed_time():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    elapsed_seconds = end_time - start_time
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)
    print(f"Total time elapsed today: {hours:02d}:{minutes:02d}:{seconds:02d}")
if __name__ == '__main__':
    calculate_elapsed_time()