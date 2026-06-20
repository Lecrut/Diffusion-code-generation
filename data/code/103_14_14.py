from datetime import datetime

def format_elapsed_time(start_time, end_time):
    elapsed = end_time - start_time
    hours = elapsed.seconds // 3600
    minutes = (elapsed.seconds % 3600) // 60
    seconds = elapsed.seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    start_time = datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.now()
    print(format_elapsed_time(start_time, end_time))