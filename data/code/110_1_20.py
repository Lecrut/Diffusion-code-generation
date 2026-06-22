from datetime import datetime

def sort_datetimes(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    d1 = datetime(2023, 1, 1)
    d2 = datetime(2023, 12, 31)
    d3 = datetime(2023, 6, 15)
    result = sort_datetimes([d2, d1, d3])
    print(result)