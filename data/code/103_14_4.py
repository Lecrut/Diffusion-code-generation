from datetime import datetime

def format_elapsed_time(start_time: datetime, end_time: datetime) -> str:
    elapsed = end_time - start_time
    hours, remainder = divmod(elapsed.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    sample_start_time = datetime(2023, 4, 1, 9, 0, 0)
    sample_end_time = datetime.now()
    print(format_elapsed_time(sample_start_time, sample_end_time))