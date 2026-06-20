from datetime import datetime

def is_earlier(date1, date2):
    return date1 < date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 2)
    print(is_earlier(sample_date1, sample_date2))