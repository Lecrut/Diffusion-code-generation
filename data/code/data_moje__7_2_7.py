def convert_time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Input must be in H:M:S format")
    hours, minutes, seconds = map(int, parts)
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_time = '1:30:45'
    print(convert_time_to_seconds(sample_time))