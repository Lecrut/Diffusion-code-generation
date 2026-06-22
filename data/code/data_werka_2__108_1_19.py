def get_day_of_month(timestamp):
    import calendar
    import datetime
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.day

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_of_month(sample_timestamp)
    print(result)