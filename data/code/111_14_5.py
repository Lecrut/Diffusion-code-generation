from datetime import datetime

def format_datetime():
    dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_dt

if __name__ == '__main__':
    print(format_datetime())