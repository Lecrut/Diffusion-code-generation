from datetime import datetime

def format_elapsed_time():
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    hours, remainder = divmod(elapsed_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(format_elapsed_time())