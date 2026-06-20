import time

def find_weekday_from_date(date):
    timestamp = time.mktime(time.strptime(date, '%Y-%m-%d'))
    weekday = time.strftime('%A', time.localtime(timestamp))
    return weekday

if __name__ == '__main__':
    sample_date_1 = '2023-01-01'
    weekday_1 = find_weekday_from_date(sample_date_1)
    print(f"Date: {sample_date_1}, Weekday: {weekday_1}")
    
    sample_date_2 = '2022-12-25'
    weekday_2 = find_weekday_from_date(sample_date_2)
    print(f"Date: {sample_date_2}, Weekday: {weekday_2}")