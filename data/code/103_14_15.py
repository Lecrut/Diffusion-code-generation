from datetime import datetime

def get_elapsed_time():
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    hours = elapsed_time.seconds // 3600
    minutes = (elapsed_time.seconds % 3600) // 60
    seconds = elapsed_time.seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(get_elapsed_time())