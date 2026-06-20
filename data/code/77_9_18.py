def time_to_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid time format")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        return hours * 60 + minutes + (seconds / 60.0)
    except (ValueError, TypeError):
        raise ValueError("Invalid time format")

if __name__ == '__main__':
    print(time_to_minutes("1:30:45"))
    print(time_to_minutes("2:15"))