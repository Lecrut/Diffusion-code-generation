import datetime
import time
def calculate_seconds_since_epoch(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    epoch = datetime.datetime(1970, 1, 1)
    time_difference = date_obj - epoch
    return int(time_difference.total_seconds())
if __name__ == '__main__':
    sample_date = "2023-10-27"
    elapsed_seconds = calculate_seconds_since_epoch(sample_date)
    print(elapsed_seconds)