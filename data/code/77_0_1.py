import datetime
def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + s
    return total_minutes
if __name__ == '__main__':
    sample_time = "01:30:45"
    result = time_to_minutes(sample_time)
    print(result)