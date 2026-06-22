import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    start_format = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_time_str, start_format)
    end_dt = datetime.strptime(end_time_str, start_format)
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    
    if output_unit == 'minutes':
        return total_seconds / 60
    elif output_unit == 'hours':
        return total_seconds / 3600
    elif output_unit == 'seconds':
        return total_seconds
    else:
        raise ValueError(f"Unsupported unit: {output_unit}")

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument('--start', type=str, required=True, help="Start time in format YYYY-MM-DD HH:MM:SS")
    parser.add_argument('--end', type=str, required=True, help="End time in format YYYY-MM-DD HH:MM:SS")
    parser.add_argument('--unit', type=str, required=True, choices=['seconds', 'minutes', 'hours'], help="Output unit")
    
    args = parser.parse_args()
    
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)

if __name__ == '__main__':
    start_val = "2023-10-01 10:00:00"
    end_val = "2023-10-01 12:30:45"
    unit_val = "minutes"
    
    result = calculate_elapsed_time(start_val, end_val, unit_val)
    print(result)