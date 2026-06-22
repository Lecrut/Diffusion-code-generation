import datetime

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    format_str = '%H:%M'
    try:
        time1 = datetime.datetime.strptime(time_str1, format_str)
        time2 = datetime.datetime.strptime(time_str2, format_str)
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM'.")

    time_difference = abs((time2 - time1).total_seconds())
    return int(time_difference)

if __name__ == '__main__':
    sample_time1 = '14:30'
    sample_time2 = '16:45'
    print(calculate_time_difference(sample_time1, sample_time2))