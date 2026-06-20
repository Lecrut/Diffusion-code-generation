import datetime

def calculate_elapsed_time():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed_time = now - midnight
    return str(elapsed_time).split('.')[0]

if __name__ == '__main__':
    print(calculate_elapsed_time())