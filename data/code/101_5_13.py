import time

def find_day_of_week_from_date(date_str):
    timestamp = int(time.mktime(time.strptime(date_str, '%Y-%m-%d')))
    return time.strftime('%A', time.localtime(timestamp))

if __name__ == '__main__':
    sample_date_1 = '2023-01-01'
    print(f"Date {sample_date_1}: {find_day_of_week_from_date(sample_date_1)}")