def time_to_minutes(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 60 + minutes + seconds / 60

@time_to_minutes
def convert_duration_to_minutes(duration_str):
    return duration_str

if __name__ == '__main__':
    durations = ['1:30:00', '0:05:45', '2:15:45']
    for duration in durations:
        result = convert_duration_to_minutes(duration)
        print(result)