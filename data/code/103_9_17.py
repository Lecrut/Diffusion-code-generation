import datetime

def calculate_elapsed_time():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = now - start_of_day
    return f"{elapsed_time.seconds // 3600:02}:{(elapsed_time.seconds % 3600) // 60:02}:{elapsed_time.seconds % 60:02}"

if __name__ == '__main__':
    print(calculate_elapsed_time())