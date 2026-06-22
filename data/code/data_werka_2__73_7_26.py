from datetime import datetime

def calculate_minutes_difference(first_date_str, second_date_str):
    date_format = '%Y-%m-%d %H:%M:%S'
    first_datetime = datetime.strptime(first_date_str, date_format)
    second_datetime = datetime.strptime(second_date_str, date_format)
    time_delta = second_datetime - first_datetime
    total_seconds = time_delta.total_seconds()
    minutes_difference = total_seconds / 60
    return minutes_difference

if __name__ == '__main__':
    start_time = '2024-05-10 08:15:30'
    end_time = '2024-05-10 09:45:30'
    diff_minutes = calculate_minutes_difference(start_time, end_time)
    print(diff_minutes)