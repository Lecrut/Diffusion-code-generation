from datetime import datetime

def validate_time(time_str):
    try:
        return datetime.strptime(time_str, '%H:%M')
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM'.")

def calculate_time_difference(start_time_str, end_time_str):
    start_time = validate_time(start_time_str)
    end_time = validate_time(end_time_str)
    
    if start_time > end_time:
        end_time += datetime.strptime('24:00', '%H:%M')
    
    return (end_time - start_time).seconds // 60

if __name__ == '__main__':
    sample_start_time = '23:59'
    sample_end_time = '00:01'
    difference_in_minutes = calculate_time_difference(sample_start_time, sample_end_time)
    print(difference_in_minutes)