from datetime import datetime

def format_datetime():
    sample_datetime = datetime(2023, 9, 15, 14, 30, 0)
    formatted_string = sample_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_string

if __name__ == '__main__':
    print(format_datetime())