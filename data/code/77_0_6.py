def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        if h < 0 or m < 0 or s < 0:
            raise ValueError("Time components must be non-negative")
        total_minutes = h * 60 + m + s / 60
        return total_minutes
    except (ValueError, TypeError):
        raise ValueError("Invalid time format. Expected 'HH:MM:SS'")

if __name__ == '__main__':
    sample_time = "14:30:15"
    result = time_to_minutes(sample_time)
    print(result)