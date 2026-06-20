import datetime

def calculate_time_difference(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%Y-%m-%d %H:%M:%S'
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        time_difference = abs(date1 - date2)
        return int(time_difference.total_seconds())
    except ValueError:
        return -1

if __name__ == '__main__':
    sample_date1 = "2023-10-27 11:45:00"
    sample_date2 = "2023-10-27 11:50:30"
    difference_seconds = calculate_time_difference(sample_date1, sample_date2)
    print(difference_seconds)