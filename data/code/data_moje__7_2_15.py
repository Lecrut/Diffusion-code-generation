def convert_time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '0:00:00', '24:00:00', '12:30:30']
    for t in sample_times:
        print(convert_time_to_seconds(t))