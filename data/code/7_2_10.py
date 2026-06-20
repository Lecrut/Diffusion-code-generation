def duration_to_seconds(time_string):
    parts = time_string.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

if __name__ == '__main__':
    time_input = '1:30:45'
    result = duration_to_seconds(time_input)
    print(result)