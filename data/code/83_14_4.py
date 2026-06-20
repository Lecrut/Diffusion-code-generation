from datetime import datetime

def are_datetimes_equal(dt1, dt2):
    return dt1 == dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 5, 14, 30)
    sample_dt2 = datetime(2023, 10, 5, 14, 30)
    print(are_datetimes_equal(sample_dt1, sample_dt2))