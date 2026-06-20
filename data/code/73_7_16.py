import datetime

def calculate_time_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d %H:%M:%S"
    date_obj1 = datetime.datetime.strptime(date_str1, date_format)
    date_obj2 = datetime.datetime.strptime(date_str2, date_format)
    difference = abs((date_obj2 - date_obj1).total_seconds())
    return int(difference / 60)

if __name__ == '__main__':
    sample_date_a = "2023-09-15 14:45:00"
    sample_date_b = "2023-09-15 17:30:00"
    minutes_difference = calculate_time_difference(sample_date_a, sample_date_b)
    print(minutes_difference)