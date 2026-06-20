import datetime

def format_custom_datetime():
    dt = datetime.datetime(2023, 11, 20, 18, 45, 0)
    formatted_dt = dt.strftime('%A, %B %d, %Y %I:%M %p')
    return formatted_dt

if __name__ == '__main__':
    print(format_custom_datetime())