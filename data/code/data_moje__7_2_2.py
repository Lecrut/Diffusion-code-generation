def convert_time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2]) if len(parts) == 3 else 0
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '2:00:00', '0:05:30', '12:15:45']
    for t in sample_times:
        print(convert_time_to_seconds(t))