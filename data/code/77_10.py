import sys
def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes + seconds / 60
        return int(total_minutes)
    except ValueError:
        return -1
if __name__ == '__main__':
    sample_time = "01:30:45"
    result = time_to_minutes(sample_time)
    print(result)