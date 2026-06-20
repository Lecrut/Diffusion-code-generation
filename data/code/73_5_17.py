import datetime

def calculate_duration(date1, date2):
    time_difference = abs(date2 - date1)
    return time_difference.total_seconds()

if __name__ == '__main__':
    date_str1 = '2023-10-05 14:00:00'
    date_str2 = '2023-10-06 18:30:00'
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
    print(calculate_duration(date1, date2))