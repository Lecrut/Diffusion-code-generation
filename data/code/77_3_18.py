def parse_time(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Incorrect number of time components")
        hours, minutes, seconds = map(int, parts)
        return hours, minutes, seconds
    except (ValueError, TypeError):
        raise ValueError("Invalid time format")

def calculate_total_minutes(time_str):
    try:
        hours, minutes, seconds = parse_time(time_str)
        total_minutes = hours * 60 + minutes + seconds // 60
        return total_minutes
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    time1 = "1:30:00"
    time2 = "23:59:59"
    
    print(calculate_total_minutes(time1))
    print(calculate_total_minutes(time2))
    print(calculate_total_minutes("24:00:00"))
    print(calculate_total_minutes("12:60:00"))