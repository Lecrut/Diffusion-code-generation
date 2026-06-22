def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_duration(start_time, end_time):
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    duration = (end_minutes - start_minutes) % (24 * 60)
    return duration

if __name__ == '__main__':
    print(calculate_duration('07:45', '18:23'))