def time_to_seconds(time_str: str) -> int:
    parts = time_str.strip().split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in H:M:S format")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_times = ['1:30:45', '0:0:0', '2:45:10', '10:30:00']
    for t in sample_times:
        result = time_to_seconds(t)
        print(result)