import time

def elapsed_time():
    start = 0
    current = time.time()
    elapsed_seconds = int(current - start)
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(elapsed_time())