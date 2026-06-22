def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '2:15:30', '0:45:00']
    for time in sample_times:
        print(time_to_seconds(time))