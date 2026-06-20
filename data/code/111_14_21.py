import datetime

def format_datetime():
    dt = datetime.datetime(2023, 9, 15, 14, 30, 0)
    if not isinstance(dt, datetime.datetime):
        raise ValueError("Provided value is not a valid datetime object")

    formatted_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_dt

if __name__ == '__main__':
    print(format_datetime())