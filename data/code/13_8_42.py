from datetime import timedelta

def parse_time_difference(time_str):
    total_seconds = 0
    parts = time_str.split()
    
    for i in range(0, len(parts), 2):
        value = int(parts[i])
        unit = parts[i + 1].lower()
        
        if unit == 'seconds':
            total_seconds += value
        elif unit == 'minutes':
            total_seconds += value * 60
        elif unit == 'hours':
            total_seconds += value * 3600
        elif unit == 'days':
            total_seconds += value * 86400
        else:
            raise ValueError(f"Unsupported time unit: {unit}")
    
    return timedelta(seconds=total_seconds)

def calculate_total_minutes(time_differences):
    total_timedelta = timedelta()
    
    for time_str in time_differences:
        total_timedelta += parse_time_difference(time_str)
    
    return int(total_timedelta.total_seconds() / 60)

if __name__ == '__main__':
    sample_times = [
        '2 hours 30 minutes',
        '1 hour 45 minutes',
        '30 minutes',
        '1 day 2 hours'
    ]
    
    total_minutes = calculate_total_minutes(sample_times)
    print(total_minutes)