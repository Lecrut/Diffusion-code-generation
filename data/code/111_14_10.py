from datetime import datetime

def format_datetime():
    dt = datetime(2023, 9, 15, 14, 30, 0)
    date_format = "%Y-%m-%d %H:%M:%S"
    formatted_dt = dt.strftime(date_format)
    return formatted_dt

if __name__ == '__main__':
    print(format_datetime())