import time

def elapsed_time_since_midnight():
    current_time = time.time()
    midnight = time.mktime(current_time // 86400 * 86400)
    seconds_elapsed = int(current_time - midnight)
    hours = seconds_elapsed // 3600
    minutes = seconds_elapsed % 3600 // 60
    seconds = seconds_elapsed % 60
    return f'{hours}h {minutes}m {seconds}s'
if __name__ == '__main__':
    print(elapsed_time_since_midnight())