from datetime import datetime

def sort_datetimes(datetime_list):
    return sorted(datetime_list)

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 15, 10, 30)
    dt2 = datetime(2022, 12, 1, 8, 0)
    dt3 = datetime(2023, 6, 20, 14, 45)
    dt4 = datetime(2021, 11, 5, 9, 15)
    
    original_list = [dt1, dt2, dt3, dt4]
    sorted_list = sort_datetimes(original_list)
    
    print(sorted_list)