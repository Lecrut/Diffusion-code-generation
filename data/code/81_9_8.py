def calculate_elapsed_hours(time1, time2):
    try:
        h1, m1, s1 = map(int, time1.split(':'))
        h2, m2, s2 = map(int, time2.split(':'))
        
        total_seconds_1 = h1 * 3600 + m1 * 60 + s1
        total_seconds_2 = h2 * 3600 + m2 * 60 + s2
        
        return abs(total_seconds_2 - total_seconds_1) / 3600.0
    
    except (ValueError, TypeError):
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

if __name__ == '__main__':
    sample_time1 = "12:34:56"
    sample_time2 = "18:45:01"
    result = calculate_elapsed_hours(sample_time1, sample_time2)
    print(f"Elapsed hours between {sample_time1} and {sample_time2}: {result:.2f}")