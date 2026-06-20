from datetime import datetime

def compare_datetimes(dt1, dt2):
    if dt1 < dt2:
        return 'First is earlier'
    elif dt1 > dt2:
        return 'Second is earlier'
    else:
        return 'They are equal'

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2023, 1, 2)
    print(compare_datetimes(dt1, dt2))