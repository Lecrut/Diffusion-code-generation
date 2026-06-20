import time

def timestamp_to_date(timestamp):
    return time.localtime(timestamp)

def date_to_weekday(date_tuple):
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return weekdays[date_tuple.tm_wday]

if __name__ == '__main__':
    sample_timestamp = 1678886400
    sample_date = timestamp_to_date(sample_timestamp)
    weekday = date_to_weekday(sample_date)
    print(f"Timestamp: {sample_timestamp}, Day of Week: {weekday}")