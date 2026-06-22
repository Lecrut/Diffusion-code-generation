def convert_time_to_seconds(time_string):
    parts = time_string.split(':')
    if len(parts) != 3:
        raise ValueError("Time must be in H:M:S format")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '0:0:1', '24:0:0', '0:1:0']
    for time_val in sample_times:
        result = convert_time_to_seconds(time_val)
        print(result)