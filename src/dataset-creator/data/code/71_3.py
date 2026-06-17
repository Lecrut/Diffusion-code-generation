import argparse
def parse_time_to_seconds(time_str):
    try:
        value = float(time_str)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid input '{time_str}': must be a numeric value.")
    unit_map = {
        'ms': 1e-3,
        's': 1.0,
        'm': 60.0,
        'h': 3600.0,
        'd': 86400.0,
    }
    if not time_str.endswith(unit_map.keys()):
        raise argparse.ArgumentTypeError(f"Invalid unit '{time_str[-1]}'. Supported units: ms, s, m, h, d.")
    multiplier = unit_map[time_str[-1]]
    return value * multiplier
def parse_seconds_to_time(seconds):
    try:
        if not isinstance(seconds, (int, float)):
            raise argparse.ArgumentTypeError(f"Invalid input '{seconds}': must be numeric.")
        total_ms = int(round(seconds * 1000))
        days = total_ms // (86400 * 1000)
        remaining_ms = total_ms % (86400 * 1000)
        hours = remaining_ms // (3600 * 1000)
        remaining_ms %= (3600 * 1000)
        minutes = remaining_ms // (60 * 1000)
        seconds_part = round(remaining_ms / 1000, 2)
    except Exception:
        raise argparse.ArgumentTypeError(f"Invalid input '{seconds}': must be numeric.")
    if days > 0:
        return f"{days}d {hours}:{minutes:02d}:{seconds_part:.2f}"
    elif hours > 0:
        return f"{hours}h {minutes}:{seconds_part:.2f}"
    else:
        return f"{minutes}m {seconds_part:.2f}s"
def main():
    parser = argparse.ArgumentParser(description="Convert time units to seconds and vice versa.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    convert_to_sec_parser = subparsers.add_parser('to-seconds', help='Convert time unit to seconds.')
    convert_to_sec_parser.add_argument(
        'time_input', type=parse_time_to_seconds, nargs='+', metavar=('VALUE', 'UNIT'),
        help="Time value and optional unit (e.g., 100 ms or 2 h)"
    )
    convert_from_sec_parser = subparsers.add_parser('from-seconds', help='Convert seconds to time units.')
    convert_from_sec_parser.add_argument(
        'seconds_input', type=parse_seconds_to_time, nargs='+', metavar=('VALUE'),
        help="Seconds value (e.g., 3601.5)"
    )
    args = parser.parse_args()
    if not hasattr(args, 'command') or args.command is None:
        parser.print_help()
        return
    if args.command == 'to-seconds':
        for val_unit in args.time_input:
            value_str, unit_str = str(val_unit).split(' ', 1)
            try:
                seconds = float(value_str) * parse_time_to_seconds(unit_str)[0] / (parse_time_to_seconds(unit_str)[-2]) if isinstance(parse_time_to_seconds(unit_str), tuple) else None
            except Exception as e:
                print(f"Error converting {val_unit}: {e}")
    elif args.command == 'from-seconds':
        for val in args.seconds_input:
            try:
                time_obj = parse_seconds_to_time(val)[0] if isinstance(parse_seconds_to_time(val), tuple) else None
            except Exception as e:
                print(f"Error converting {val}: {e}")
if __name__ == '__main__':
    main()