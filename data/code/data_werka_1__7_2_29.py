def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '2:45:30', '0:15:20']
    for time in sample_times:
        print(convert_to_seconds(time))