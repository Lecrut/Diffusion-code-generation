from datetime import datetime

def calculate_elapsed_seconds():
    current_time = datetime.now()
    today_midnight = datetime.combine(current_time.date(), datetime.min.time())
    elapsed_seconds = (current_time - today_midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 5, 14, 30, 0)
    print(calculate_elapsed_seconds())