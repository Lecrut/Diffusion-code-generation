def duration_to_seconds(duration_str):
    parts = duration_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format")
    hours, minutes, seconds = parts
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds

if __name__ == '__main__':
    time_input = '1:30:45'
    result = duration_to_seconds(time_input)
    print(result)