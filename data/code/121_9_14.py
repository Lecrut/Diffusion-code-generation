from datetime import datetime

def compare_datetimes(dt1, dt2):
    return dt1 > dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 15, 14, 30)
    sample_dt2 = datetime(2023, 10, 15, 14, 29)
    result = compare_datetimes(sample_dt1, sample_dt2)
    print(result)