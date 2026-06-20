import time

SECONDS_IN_DAY = 24 * 60 * 60

def calculate_elapsed_time():
    current_time = time.time()
    elapsed_seconds = current_time % SECONDS_IN_DAY
    return elapsed_seconds / SECONDS_IN_DAY

if __name__ == '__main__':
    result = calculate_elapsed_time()
    print(result)