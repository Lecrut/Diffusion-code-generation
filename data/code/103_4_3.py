import datetime
def calculate_time_elapsed(date_obj):
    now = datetime.datetime.now()
    time_elapsed = now - date_obj
    return time_elapsed
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 1, 1, 10, 0, 0)
    elapsed_time = calculate_time_elapsed(sample_date)
    print(elapsed_time)