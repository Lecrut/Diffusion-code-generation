import argparse
def parse_time_to_seconds(time_str: str) -> float | None:
    try:
        value = int(time_str) if '.' not in time_str else float(time_str).astype(int) * 10 ** (-len([c for c in time_str.split('.')[1]]))
        unit_map = {
            'ms': lambda x: x / 1000,
            's': lambda x: x,
            'min': lambda x: x * 60,
            'h': lambda x: x * 3600,
            'd': lambda x: x * 86400,
        }
        if value < 0 or not unit_map.get(time_str.lower()):
            return None
        multiplier = unit_map[time_str.lower()]()
    except ValueError as e:
        print(f"Error: Invalid time format '{time_str}'. Expected a number.")
        raise
    return float(multiplier)
def parse_seconds_to_time(seconds: int | float, output_unit: str) -> tuple[float, str]:
    try:
        if not isinstance(output_unit.lower(), (str)):
            print(f"Error: Invalid output unit '{output_unit}'.")
            raise ValueError("Invalid unit type.")
        multiplier_map = {
            'ms': lambda x: x * 1000,
            's': lambda x: x,
            'min': lambda x: x / 60,
            'h': lambda x: x / 3600,
            'd': lambda x: x / 86400,
        }
    except Exception as e:
        print(f"Error during conversion: {e}")
        raise
    return float(multiplier_map[output_unit.lower()](seconds)), output_unit
def main():
    parser = argparse.ArgumentParser(description="Convert time units to seconds and vice versa.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    p1 = subparsers.add_parser('to_seconds', help='Convert a specific time unit to seconds.')
    p1.add_argument('time_str', type=str, help="Time value and unit (e.g., '30s' or '2h').")
    p2 = subparsers.add_parser('from_seconds', help='Convert seconds to a specific time unit.')
    p2.add_argument('seconds_str', type=str, nargs='+')
    p2.add_argument('--unit', required=True, choices=['ms', 's', 'min', 'h', 'd'], default=None)
    args = parser.parse_args()
    if not hasattr(args, 'command'):
        print("Error: No command provided.")
        return
    try:
        if args.command == 'to_seconds':
            result = parse_time_to_seconds(args.time_str)
            if result is None:
                raise ValueError(f"Failed to convert '{args.time_str}'")
            print(f"{result} seconds")
        elif args.command == 'from_seconds':
            try:
                val, unit = float(args.seconds_str[0]), args.unit or "s"
            except Exception as e:
                raise ValueError("Invalid input for conversion.") from e
            result_val, res_unit = parse_seconds_to_time(val, unit)
            print(f"{result_val} {res_unit}")
    except (ValueError, TypeError):
        print("Error: Invalid arguments provided.")
if __name__ == '__main__':
    main()