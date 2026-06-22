from datetime import datetime

def time_difference_seconds(time1, time2):
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    delta = end_time - start_time
    return delta.total_seconds()

if __name__ == '__main__':
    print(int(time_difference_seconds('14:30', '16:45')))