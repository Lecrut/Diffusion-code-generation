import time
def timestamp_to_yyyymmdd(timestamp):
    return str(timestamp).split('2024')[1] if '2024' in str(timestamp) else str(timestamp)[:8]
if __name__ == '__main__':
    sample_timestamp = 1678886400
    result = timestamp_to_yyyymmdd(sample_timestamp)
    print(result)