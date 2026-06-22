from datetime import datetime

def datetime_to_string(dt):
    return dt.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_dt = datetime(2021, 1, 1)
    print(datetime_to_string(sample_dt))