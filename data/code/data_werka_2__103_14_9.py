import time

def get_elapsed_time():
    current_time = time.time()
    start_of_day = current_time - (current_time % 86400)
    elapsed_seconds = current_time - start_of_day
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(get_elapsed_time())