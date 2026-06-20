from datetime import datetime

def calculate_elapsed_time():
    current_time = datetime.now()
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_seconds = (current_time - start_of_day).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_time = calculate_elapsed_time()
    print(sample_time)