import argparse
def calculate_duration(start_time_str, end_time_str, unit):
    start_time = float(start_time_str)
    end_time = float(end_time_str)
    duration = end_time - start_time
    if unit == 'minutes':
        result = duration / 60.0
    elif unit == 'seconds':
        result = duration
    else:
        raise ValueError("Unsupported unit. Please use 'minutes' or 'seconds'.")
    return result
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate elapsed time between start and end times.")
    parser.add_argument("start_time", type=str, help="Start time in a numerical format.")
    parser.add_argument("end_time", type=str, help="End time in a numerical format.")
    parser.add_argument("unit", type=str, choices=['minutes', 'seconds'], help="Desired output unit ('minutes' or 'seconds').")
    args = parser.parse_args(["100", "120", "minutes"])
    try:
        result = calculate_duration(args.start_time, args.end_time, args.unit)
        print(f"Elapsed time: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")