import datetime
def calculate_time_difference(date_str1, date_str2):
    format_str = '%Y-%m-%d %H:%M:%S'
    dt1 = datetime.datetime.strptime(date_str1, format_str)
    dt2 = datetime.datetime.strptime(date_str2, format_str)
    time_difference = abs(dt1 - dt2)
    total_minutes = int(time_difference.total_seconds() / 60)
    return total_minutes
if __name__ == '__main__':
    date1 = '2023-01-01 10:00:00'
    date2 = '2023-01-01 11:30:45'
    result = calculate_time_difference(date1, date2)
    print(result)