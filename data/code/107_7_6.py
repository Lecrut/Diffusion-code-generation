import datetime

def convert_timestamp(timestamp: int) -> str:
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    result = convert_timestamp(1609459200)
    print(result)