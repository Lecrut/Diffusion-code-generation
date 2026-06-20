import datetime

def compare_datetimes_ignoring_time(dt1, dt2):
    return dt1.date() == dt2.date()
if __name__ == '__main__':
    sample_dt1 = datetime.datetime(2023, 4, 15, 12, 30, 0)
    sample_dt2 = datetime.datetime(2023, 4, 15, 18, 45, 0)
    print(compare_datetimes_ignoring_time(sample_dt1, sample_dt2))