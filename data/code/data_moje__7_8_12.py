import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    time_format = "%Y-%m-%d %H:%M:%S"
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if output_unit == 'seconds':
        return total_seconds
    elif output_unit == 'minutes':
        return total_seconds / 60
    elif output_unit == 'hours':
        return total_seconds / 3600
    elif output_unit == 'days':
        return total_seconds / 86400
    else:
        raise ValueError(f"Unknown output unit: {output_unit}")

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument('--start-time', type=str, default='2023-01-01 10:00:00', help="Start time in format YYYY-MM-DD HH:MM:SS")
    parser.add_argument('--end-time', type=str, default='2023-01-01 12:30:00', help="End time in format YYYY-MM-DD HH:MM:SS")
    parser.add_argument('--unit', type=str, default='minutes', choices=['seconds', 'minutes', 'hours', 'days'], help="Output unit for elapsed time")
    
    args = parser.parse_args()
    
    result = calculate_elapsed_time(args.start_time, args.end_time, args.unit)
    print(result)

if __name__ == '__main__':
    main()