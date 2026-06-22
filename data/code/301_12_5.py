from datetime import datetime

def format_datetime(dt):
    return dt.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_dt = datetime(2021, 1, 1)
    print(format_datetime(sample_dt))