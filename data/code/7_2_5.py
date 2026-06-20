def time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format. Expected H:M:S")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_input = '1:30:45'
    result = time_to_seconds(sample_input)
    print(result)