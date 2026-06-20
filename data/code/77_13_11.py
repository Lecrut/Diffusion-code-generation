def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return (hours * 60) | minutes

if __name__ == '__main__':
    sample_times = ['12:34', '09:59', '23:00']
    for time in sample_times:
        print(time_to_minutes(time))