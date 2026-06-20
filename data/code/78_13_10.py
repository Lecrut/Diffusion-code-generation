import time

def month_difference(timestamp1, timestamp2):
    date1 = time.localtime(timestamp1)
    date2 = time.localtime(timestamp2)
    
    year_diff = date2.tm_year - date1.tm_year
    month_diff = date2.tm_mon - date1.tm_mon
    
    return year_diff * 12 + month_diff

if __name__ == '__main__':
    timestamp1 = int(time.mktime((2022, 1, 15, 0, 0, 0, 0, 0, 0)))
    timestamp2 = int(time.mktime((2023, 4, 20, 0, 0, 0, 0, 0, 0)))
    
    print(month_difference(timestamp1, timestamp2))