def time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time format must be H:M:S")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '0:0:0', '23:59:59', '0:1:30', '12:0:0']
    for t in sample_times:
        print(time_to_seconds(t))