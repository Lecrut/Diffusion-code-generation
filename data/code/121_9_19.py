from datetime import datetime

def compare_datetime(dt1, dt2):
    if dt1 > dt2:
        return "dt1 is later"
    elif dt1 < dt2:
        return "dt2 is later"
    else:
        return "Both datetimes are the same"

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1)
    dt2 = datetime(2023, 9, 30)
    result = compare_datetime(dt1, dt2)
    print(result)