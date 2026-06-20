import argparse
from datetime import datetime, timedelta

def calculate_elapsed_time(start_time_str, end_time_str, unit):
    start_time = datetime.fromisoformat(start_time_str)
    end_time = datetime.fromisoformat(end_time_str)
    
    if end_time < start_time:
        raise ValueError("End time must be after start time")
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if unit == 'seconds':
        return total_seconds
    elif unit == 'minutes':
        return total_seconds / 60
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'days':
        return total_seconds / 86400
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def main():
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two times.')
    parser.add_argument('--start', type=str, required=False, help='Start time in ISO format')
    parser.add_argument('--end', type=str, required=False, help='End time in ISO format')
    parser.add_argument('--unit', type=str, required=False, help='Output unit (seconds, minutes, hours, days)')
    
    args = parser.parse_args()
    
    sample_start = "2023-10-01T10:00:00"
    sample_end = "2023-10-01T10:35:45"
    sample_unit = "minutes"
    
    if args.start is not None:
        sample_start = args.start
    if args.end is not None:
        sample_end = args.end
    if args.unit is not None:
        sample_unit = args.unit
    
    result = calculate_elapsed_time(sample_start, sample_end, sample_unit)
    print(result)

if __name__ == '__main__':
    main()