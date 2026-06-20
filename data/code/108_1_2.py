def get_day_of_month(timestamp):
    return timestamp.day

if __name__ == '__main__':
    from datetime import datetime
    sample_timestamp = datetime(2023, 9, 15)
    print(get_day_of_month(sample_timestamp))