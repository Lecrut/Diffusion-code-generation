from datetime import datetime

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    dt = datetime(2023, 9, 15, 14, 30, 0)
    formatted_dt = format_datetime(dt)
    print(formatted_dt)