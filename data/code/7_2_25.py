def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_time1 = '1:30:45'
    sample_time2 = '2:45:10'
    print(time_to_seconds(sample_time1))
    print(time_to_seconds(sample_time2))