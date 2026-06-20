import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
        time_difference = abs(date1 - date2)
        return int(time_difference.total_seconds())
    except ValueError:
        return -1

if __name__ == '__main__':
    sample_date1 = "2023-10-28 14:30:00"
    sample_date2 = "2023-10-27 12:00:00"
    diff_seconds = calculate_time_difference(sample_date1, sample_date2)
    print(diff_seconds)