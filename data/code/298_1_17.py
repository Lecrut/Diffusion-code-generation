from datetime import datetime

def time_difference_seconds(time1_str, time2_str):
    format_str = "%H:%M"
    time1 = datetime.strptime(time1_str, format_str)
    time2 = datetime.strptime(time2_str, format_str)
    tdelta = time2 - time1
    return tdelta.total_seconds()

if __name__ == '__main__':
    sample_time1 = "14:30"
    sample_time2 = "16:45"
    result = time_difference_seconds(sample_time1, sample_time2)
    print(result)