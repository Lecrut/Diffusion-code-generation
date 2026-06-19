def parse_time_difference(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60

def aggregate_durations(time_diffs):
    total_seconds = sum(parse_time_difference(td) for td in time_diffs)
    return total_seconds

if __name__ == '__main__':
    sample_times = ['1:30', '2:45', '0:15']
    total_duration = aggregate_durations(sample_times)
    print(total_duration)