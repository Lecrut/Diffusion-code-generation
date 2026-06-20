def calculate_time_difference(start_time_str: str, end_time_str: str) -> float:
    start_hours, start_minutes, start_seconds = map(int, start_time_str.split(':'))
    end_hours, end_minutes, end_seconds = map(int, end_time_str.split(':'))
    
    start_total_seconds = start_hours * 3600 + start_minutes * 60 + start_seconds
    end_total_seconds = end_hours * 3600 + end_minutes * 60 + end_seconds
    
    if end_total_seconds < start_total_seconds:
        end_total_seconds += 24 * 3600
    
    difference_seconds = end_total_seconds - start_total_seconds
    difference_hours = difference_seconds / 3600.0
    
    return difference_hours

if __name__ == '__main__':
    start_time_str = "15:45:00"
    end_time_str = "23:15:00"
    elapsed = calculate_time_difference(start_time_str, end_time_str)
    print(f"{elapsed}")