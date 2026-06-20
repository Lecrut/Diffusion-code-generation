from datetime import datetime

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    elapsed_seconds = (end_time - start_time).total_seconds()
    print(format_time(int(elapsed_seconds)))