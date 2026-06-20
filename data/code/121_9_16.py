from datetime import datetime

def later_datetime(dt1, dt2):
    if dt1 > dt2:
        return dt1
    else:
        return dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 5, 14, 30)
    sample_dt2 = datetime(2023, 10, 5, 15, 45)
    later = later_datetime(sample_dt1, sample_dt2)
    print(later)