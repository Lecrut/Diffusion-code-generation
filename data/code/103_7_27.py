import datetime

def get_elapsed_time_since_day_start():
    current_time = datetime.datetime.now()
    midnight = datetime.datetime.min.replace(year=current_time.year, month=current_time.month, day=current_time.day)
    time_delta = current_time - midnight
    return time_delta

if __name__ == '__main__':
    sample_result = get_elapsed_time_since_day_start()
    print(sample_result)