from datetime import timedelta

def parse_time_difference(time_str):
    hours = 0
    minutes = 0
    parts = time_str.split()
    
    for i in range(0, len(parts), 2):
        value = int(parts[i])
        unit = parts[i + 1].lower()
        
        if 'hour' in unit:
            hours += value
        elif 'minute' in unit:
            minutes += value
        else:
            raise ValueError(f"Unsupported time unit: {unit}")
    
    return timedelta(hours=hours, minutes=minutes)

def total_elapsed_time(time_differences):
    total_time = timedelta()
    
    for time_str in time_differences:
        total_time += parse_time_difference(time_str)
    
    return int(total_time.total_seconds() / 60)

if __name__ == '__main__':
    sample_times = [
        '2 hours 30 minutes',
        '1 hour 45 minutes',
        '30 minutes'
    ]
    
    print(total_elapsed_time(sample_times))