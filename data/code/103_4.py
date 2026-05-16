import datetime
def calculate_elapsed_time(date_object):
    now = datetime.datetime.now()
    time_difference = now - date_object
    return time_difference
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 1, 1, 10, 0, 0)
    elapsed_time = calculate_elapsed_time(sample_date)
    print(elapsed_time)