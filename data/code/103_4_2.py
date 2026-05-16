import datetime
def calculate_elapsed_time(date_obj):
    now = datetime.datetime.now()
    time_difference = now - date_obj
    return time_difference
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 1, 1, 10, 0, 0)
    elapsed = calculate_elapsed_time(sample_date)
    print(elapsed)