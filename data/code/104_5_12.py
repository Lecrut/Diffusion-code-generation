from datetime import datetime

def compare_datetimes(date1, date2):
    if date1 < date2:
        return 'First is earlier'
    elif date1 > date2:
        return 'Second is earlier'
    else:
        return 'They are equal'

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 15)
    dt2 = datetime(2023, 2, 1)
    print(compare_datetimes(dt1, dt2))
    
    dt1 = datetime(2023, 2, 1)
    dt2 = datetime(2023, 1, 15)
    print(compare_datetimes(dt1, dt2))
    
    dt1 = datetime(2023, 10, 20)
    dt2 = datetime(2023, 10, 20)
    print(compare_datetimes(dt1, dt2))