from datetime import datetime

def sort_datetimes(dates):
    return sorted(dates)

if __name__ == '__main__':
    d1 = datetime(2023, 1, 15, 10, 30)
    d2 = datetime(2022, 12, 1, 8, 0)
    d3 = datetime(2023, 6, 20, 14, 45)
    d4 = datetime(2021, 11, 5, 9, 15)
    
    original_list = [d1, d2, d3, d4]
    sorted_list = sort_datetimes(original_list)
    
    print(sorted_list)