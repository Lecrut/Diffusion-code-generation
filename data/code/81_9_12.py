def calculate_elapsed_hours(time_str1, time_str2):
    try:
        h1, m1, s1 = map(int, time_str1.split(':'))
        h2, m2, s2 = map(int, time_str2.split(':'))
        
        total_seconds_1 = h1 * 3600 + m1 * 60 + s1
        total_seconds_2 = h2 * 3600 + m2 * 60 + s2
        
        elapsed_hours = abs(total_seconds_2 - total_seconds_1) / 3600.0
        return elapsed_hours
    except ValueError:
        return None

if __name__ == '__main__':
    sample_time_1 = '14:30:00'
    sample_time_2 = '17:45:00'
    result = calculate_elapsed_hours(sample_time_1, sample_time_2)
    print(f"Elapsed hours between {sample_time_1} and {sample_time_2}: {result}")