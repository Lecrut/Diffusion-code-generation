import argparse
from datetime import datetime

def calculate_elapsed_time(start_str, end_str, unit):
    start_format = "%H:%M"
    end_format = "%H:%M"
    
    try:
        start_time = datetime.strptime(start_str, start_format)
        end_time = datetime.strptime(end_str, end_format)
    except ValueError:
        raise ValueError("Time format must be HH:MM")
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if unit == 'minutes':
        return total_seconds / 60
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'seconds':
        return total_seconds
    else:
        raise ValueError("Unsupported unit. Use 'minutes', 'hours', or 'seconds'.")

if __name__ == '__main__':
    from datetime import timedelta
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two times.")
    parser.add_argument("start_time", type=str, help="Start time in HH:MM format")
    parser.add_argument("end_time", type=str, help="End time in HH:MM format")
    parser.add_argument("output_unit", type=str, choices=['minutes', 'hours', 'seconds'], help="Desired output unit")
    
    start_sample = "09:00"
    end_sample = "17:30"
    unit_sample = "minutes"
    
    result = calculate_elapsed_time(start_sample, end_sample, unit_sample)
    print(result)