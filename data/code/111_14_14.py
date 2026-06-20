from datetime import datetime

def format_custom_datetime():
    dt = datetime(2023, 9, 15, 14, 30, 0)
    custom_format = '%A, %B %d, %Y %I:%M %p'
    formatted_dt = dt.strftime(custom_format)
    return formatted_dt

if __name__ == '__main__':
    print(format_custom_datetime())