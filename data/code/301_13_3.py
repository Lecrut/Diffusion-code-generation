import datetime
def timestamp_to_date_string(timestamp: int) -> str:
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return dt_object.strftime('%Y/%m/%d')
if __name__ == '__main__':
    sample_timestamp1 = 1678886400
    result1 = timestamp_to_date_string(sample_timestamp1)
    print(result1)
    sample_timestamp2 = 1577836800
    result2 = timestamp_to_date_string(sample_timestamp2)
    print(result2)