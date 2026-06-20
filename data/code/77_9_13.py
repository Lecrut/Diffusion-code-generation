def time_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format")
    hours, minutes, seconds = map(int, parts)
    return hours * 60 + minutes + seconds / 60

if __name__ == '__main__':
    print(time_to_minutes('1:30:45'))