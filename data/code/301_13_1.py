import datetime
def timestamp_to_date_string(timestamp: int) -> str:
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return dt_object.strftime('%Y/%m/%d')
if __name__ == '__main__':
    sample_timestamp = 1678886400
    result = timestamp_to_date_string(sample_timestamp)
    print(result)