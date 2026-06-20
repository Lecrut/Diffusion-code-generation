def validate_time_format(time_str):
    if ':' not in time_str:
        return False
    parts = time_str.split(':')
    if len(parts) != 3:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    return True

def time_to_minutes(time_str):
    if not validate_time_format(time_str):
        raise ValueError("Invalid time format. Please use HH:MM:SS.")
    
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes

if __name__ == '__main__':
    sample_time = "12:34:56"
    print(time_to_minutes(sample_time))