def convert_time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time must be in H:M:S format")
    hours, minutes, seconds = map(int, parts)
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds must be less than 60")
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_times = ["1:30:45", "0:0:1", "12:30:0", "23:59:59", "0:0:0"]
    for t in sample_times:
        result = convert_time_to_seconds(t)
        print(result)