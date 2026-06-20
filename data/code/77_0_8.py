def validate_time_format(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            raise ValueError("Invalid time format")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return True

def time_to_minutes(time_str):
    if not validate_time_format(time_str):
        return None
    
    h, m, s = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + s / 60
    return total_minutes

if __name__ == '__main__':
    sample_time = "14:30:15"
    result = time_to_minutes(sample_time)
    print(result)