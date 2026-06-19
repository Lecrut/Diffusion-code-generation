def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_time = '1:30:45'
    total_seconds = time_to_seconds(sample_time)
    print(total_seconds)