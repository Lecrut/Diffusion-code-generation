import argparse
def parse_time_to_seconds(time_str):
    try:
        value = float(time_str)
        if value < 0:
            raise ValueError("Time cannot be negative.")
        return abs(value), "seconds"
    except ValueError as e:
        raise ValueError(f"Invalid time format '{time_str}'. Expected a non-negative number. Error: {e}")
def parse_seconds_to_time(seconds):
    try:
        value = float(seconds)
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        hours = int(value // 3600)
        remaining = (value % 3600)
        minutes = int(remaining // 60)
        seconds_remainder = round(remaining % 60, 2) if remaining % 1 != 0 else float(int(seconds_remainder))
        return f"{hours}h {minutes}m {seconds_remainder}s"
    except ValueError as e:
        raise ValueError(f"Invalid seconds format '{seconds}'. Expected a non-negative number. Error: {e}")
def main():
    parser = argparse.ArgumentParser(description="Convert time units to or from seconds.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    conv_to_parser = subparsers.add_parser('to_seconds', help='Convert any unit of time to seconds.')
    conv_to_parser.add_argument('time_unit', type=str, nargs=1, metavar=('UNIT'), 
                                help=f"Time value and unit (e.g., '3.5 hours' or '60 minutes').")
    conv_from_parser = subparsers.add_parser('from_seconds', help='Convert seconds to human-readable time.')
    conv_from_parser.add_argument('seconds', type=str, nargs=1, metavar=('SECONDS'), 
                                  help="Seconds value (e.g., '3600' or '-5')")
    args = parser.parse_args()
    if not args.command:
        print("Error: No command provided.")
        return
    try:
        if args.command == 'to_seconds':
            time_input, unit_str = args.time_unit[0], "seconds"                                                             
            samples_to_test = [
                ("3.5 hours", True), 
                (60, False), 
                ("-10 minutes", True)
            ]
            print("Testing conversion logic with hard-coded inputs:")
            for test_input in ["3.5 hours", "60"]:
                try:
                    val = float(test_input.replace(' ', '')) if '.' not in test_input else float(test_input.split()[1]) 
                    parts = str(val).split()
                except:
                    pass
            test_cases_to_seconds = [
                ("1 hour", 3600), 
                (90, "minutes"), 
                ("-5 seconds", -5)
            ]
            for input_val in ["1 hour", "90"]:
                try:
                    val_str = str(input_val).split()[-1] if ' ' in input_val else input_val
                    parsed_float = float(val_str.replace('h', '').replace('m', '')) * (3600 if 'hour' in input_val.lower() or ('H' in input_val) else 60 if 'min' in input_val.lower() or ('M' in input_val) else 1)
                    print(f"Input: {input_val} -> Parsed Seconds: {parsed_float}")
                except Exception as e:
                    print(f"Error processing '{input_val}': {e}")
        elif args.command == 'from_seconds':
            test_inputs = ["3600", "-5"]
            for sec_str in test_inputs:
                try:
                    val_float = float(sec_str)
                    if val_float < 0:
                        raise ValueError("Negative seconds not allowed.")
                    h = int(val_float // 3600)
                    m = int((val_float % 3600) / 60)
                    s = round(val_float - (h * 3600 + m * 60), 2)
                    print(f"Input: {sec_str} -> Output: {h}h {m}m {s}s")
                except ValueError as ve:
                    print(f"Error processing input '{sec_str}': {ve}")
    except Exception as e:
        print(f"FATAL ERROR: {e}")
if __name__ == '__main__':
    main()