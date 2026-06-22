from datetime import datetime, time

def time_difference_in_seconds(time1_str, time2_str):
    format_str = '%H:%M:%S'
    time1 = datetime.strptime(time1_str, format_str).time()
    time2 = datetime.strptime(time2_str, format_str).time()

    def time_to_seconds(t):
        return t.hour * 3600 + t.minute * 60 + t.second
    seconds1 = time_to_seconds(time1)
    seconds2 = time_to_seconds(time2)
    difference = abs(seconds2 - seconds1)
    return difference
if __name__ == '__main__':
    sample_time1 = '14:30:00'
    sample_time2 = '09:45:00'
    print(time_difference_in_seconds(sample_time1, sample_time2))