from datetime import datetime

def format_time(elapsed_seconds):
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_elapsed_time():
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    elapsed_seconds = (end_time - start_time).total_seconds()
    return format_time(elapsed_seconds)

if __name__ == '__main__':
    elapsed = get_elapsed_time()
    print(elapsed)