from datetime import datetime

def compare_datetimes(dt1, dt2):
    if dt1 > dt2:
        return "dt1 is later"
    elif dt1 < dt2:
        return "dt2 is later"
    else:
        return "Both datetimes are the same"

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 1, 12, 0)
    sample_dt2 = datetime(2023, 9, 30, 23, 59)
    print(compare_datetimes(sample_dt1, sample_dt2))