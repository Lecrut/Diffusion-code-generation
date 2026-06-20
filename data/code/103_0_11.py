from datetime import datetime

def calculate_time_elapsed():
    current_time = datetime.now()
    midnight = datetime(current_time.year, current_time.month, current_time.day)
    time_difference = current_time - midnight
    elapsed_seconds = time_difference.total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_result = calculate_time_elapsed()
    print(sample_result)