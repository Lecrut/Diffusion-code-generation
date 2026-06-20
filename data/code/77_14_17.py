def calculate_minutes(time_str):
    if not isinstance(time_str, str) or len(time_str) != 5 or time_str[2] != ':':
        raise ValueError("Invalid time format")
    
    hours, minutes = map(int, time_str.split(':'))
    
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError("Time out of valid range")
    
    return hours * 60 + minutes

if __name__ == '__main__':
    print(calculate_minutes('14:30'))