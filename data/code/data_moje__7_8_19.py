import argparse
from datetime import datetime

def calculate_elapsed_time(start_str: str, end_str: str, unit: str) -> float:
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_str, fmt)
    end_dt = datetime.strptime(end_str, fmt)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if unit == 'seconds':
        return total_seconds
    if unit == 'minutes':
        return total_seconds / 60
    if unit == 'hours':
        return total_seconds / 3600
    if unit == 'days':
        return total_seconds / 86400
    raise ValueError(f"Unsupported unit: {unit}")

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two dates.')
    parser.add_argument('--start', type=str, required=True, help='Start time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--end', type=str, required=True, help='End time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--unit', type=str, default='seconds', choices=['seconds', 'minutes', 'hours', 'days'], help='Output unit')
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args(['--start', '2023-01-01 00:00:00', '--end', '2023-01-01 12:30:00', '--unit', 'minutes'])
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)