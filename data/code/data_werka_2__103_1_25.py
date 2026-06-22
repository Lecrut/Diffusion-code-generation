import datetime

def get_milliseconds_elapsed_today() -> int:
    now = datetime.datetime.now()
    seconds_since_midnight = (now.hour * 3600) + (now.minute * 60) + now.second
    milliseconds = (seconds_since_midnight * 1000) + (now.microsecond // 1000)
    return milliseconds

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)