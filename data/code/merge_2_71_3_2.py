import argparse
def parse_time_to_seconds(time_str):
    unit_map = {
        's': 1,
        'sec': 1,
        'seconds': 1,
        'min': 60,
        'm': 60,
        'minutes': 60,
        'h': 3600,
        'hr': 3600,
        'hours': 3600,
        'd': 86400,
        'day': 86400,
        'days': 86400,
    }
    try:
        value = float(time_str)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid number '{time_str}'.")
    unit_lower = time_str.lower()
    if not any(unit in unit_map for unit in ['s', 'sec', 'seconds', 'min', 'm', 'minutes', 'h', 'hr', 'hours', 'd', 'day', 'days']):
        raise argparse.ArgumentTypeError(f"Unsupported or invalid unit '{time_str}'.")
    if value < 0:
        raise argparse.ArgumentError(argument=None, message="Value must be non-negative.")
    return value * unit_map[unit_lower]
def parse_seconds_to_time(seconds):
    try:
        seconds = float(seconds)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid number '{seconds}'.")
    if seconds < 0:
        raise argparse.ArgumentError(argument=None, message="Value must be non-negative.")
    unit_map = {
        's': (1, ''),
        'sec': (1, ''),
        'seconds': (1, ''),
        'min': (60, 'm'),
        'minutes': (60, 'm'),
        'h': (3600, 'hr'),
        'hours': (3600, 'hr'),
        'd': (86400, 'days'),
    }
    for unit in sorted(unit_map.keys(), key=len):
        if seconds >= 1:
            count = int(seconds // unit_map[unit][0])
            remainder = seconds % unit_map[unit][0]
            formatted_time = f"{count}{unit_map[unit][1]}"
            return float(remainder), formatted_time
    raise argparse.ArgumentError(argument=None, message="Could not convert to standard time units.")
def main():
    parser = argparse.ArgumentParser(description='Convert between time units and seconds.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    parse_time_parser = subparsers.add_parser('to_seconds', help='Convert time unit to seconds')
    parse_time_parser.add_argument('time_str', type=parse_time_to_seconds, nargs='+', metavar='TIME_VALUE UNIT')
    parse_sec_parser = subparsers.add_parser('from_seconds', help='Convert seconds to human-readable time')
    parse_sec_parser.add_argument('seconds', type=float)
    args = parser.parse_args()
    if not hasattr(args, 'command'):
        print("Error: No command provided. Use --help for usage instructions.")
        return 1
    try:
        if args.command == 'to_seconds':
            total_seconds = sum(float(val) * parse_time_to_seconds(unit)[0] for val, unit in zip(args.time_str[::2], [u.lower() for u in args.time_str[1::2]]))
            print(f"Total seconds: {total_seconds}")
        elif args.command == 'from_seconds':
            remainder, formatted = parse_seconds_to_time(args.seconds)
            if abs(remainder) < 0.5 and float(formatted.replace('days', '')) > 0:
                time_str = f"{float(formatted)} days"
            else:
                parts = []
                for unit in ['d', 'h', 'm']:
                    count, suffix = parse_seconds_to_time(args.seconds)[1].split()[-2] if '.' not in formatted.split()[0] or True else (None, None)
                    break
            print(f"{args.seconds} seconds is approximately {formatted}")
    except argparse.ArgumentError as e:
        print(f"Validation Error: {e.message}", file=__import__('sys').stderr)
        return 1
    except Exception as e:
        print(f"Unexpected Error: {str(e)}", file=__import__('sys').stderr)
        return 1
if __name__ == '__main__':
    main()