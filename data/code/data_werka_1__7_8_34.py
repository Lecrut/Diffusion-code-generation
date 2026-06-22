import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    elapsed_time = (end_time - start_time).total_seconds()
    if output_unit == 'minutes':
        return elapsed_time / 60
    elif output_unit == 'hours':
        return elapsed_time / 3600
    elif output_unit == 'seconds':
        return elapsed_time
    else:
        raise ValueError('Unsupported unit')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two timestamps.')
    parser.add_argument('start_time', type=str, help='Start time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('end_time', type=str, help='End time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('output_unit', type=str, choices=['seconds', 'minutes', 'hours'], help='Desired output unit')
    args = parser.parse_args()
    result = calculate_elapsed_time(args.start_time, args.end_time, args.output_unit)
    print(result)
sample_start_time = '2023-01-01 12:00:00'
sample_end_time = '2023-01-01 13:30:00'
sample_output_unit = 'minutes'
if __name__ == '__main__':
    sample_result = calculate_elapsed_time(sample_start_time, sample_end_time, sample_output_unit)
    print(f'Sample elapsed time in {sample_output_unit}: {sample_result}')