def time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 60 + minutes + seconds / 60

if __name__ == '__main__':
    sample_time = '14:30:45'
    print(time_to_minutes(sample_time))