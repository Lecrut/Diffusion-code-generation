from datetime import datetime

def later_datetime(dt1, dt2):
    if dt1 > dt2:
        return dt1
    else:
        return dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 10, 1, 14, 0, 0)
    later = later_datetime(sample_dt1, sample_dt2)
    print(f"The later datetime is: {later}")