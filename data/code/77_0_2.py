import datetime
def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_minutes = h * 60 + m + s / 60
        return total_minutes
    except ValueError:
        return None
if __name__ == '__main__':
    sample_time = "14:30:15"
    result = time_to_minutes(sample_time)
    print(result)