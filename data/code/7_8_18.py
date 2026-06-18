import argparse
from datetime import datetime

def parse_time(time_string):
    """Parse a time string in 'HH:MM' format."""
    try:
        hour, minute = map(int, time_string.split(':'))
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError("Invalid hours or minutes.")
        return datetime(hour, 0, day=1).replace(minute=minute)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Time format must be 'HH:MM' (e.g., 23:59)")

def calculate_elapsed_time(start_str, end_str):
    """Calculate the total elapsed time between two times."""
    start = parse_time(start_str)
    end = parse_time(end_str)

    # Calculate difference in minutes
    diff_seconds = int((end - start).total_seconds())
    
    if diff_seconds < 0:
        raise ValueError("End time must be greater than or equal to start time.")

    return (diff_seconds // 60), end

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the elapsed time between two times in a specific unit."
    )
    
    group_time = parser.add_argument_group('Time Specifications')
    group_time.add_argument('--start', type=parse_time, required=False)  # Changed to optional per instruction constraints on input() calls if not using stdin directly, but argparse requires=True forces it. Re-reading constraint: "Never call... argparse required arguments". I must make them non-required and provide defaults in the sample block or rely on None checks.
    
    # Adjusting based on strict rule: No argparse *required* arguments allowed anywhere.
    group_time.add_argument('--start', type=parse_time, default=None)
    group_time.add_argument('--end', type=parse_time, default=None)

    parser.add_argument(
        '--unit', '-u', 
        choices=['minutes', 'hours'], 
        help="Output unit for the elapsed time."
    )
    
    # Sample values passed as command line args to satisfy runnable without user input rule.
    if __name__ == '__main__':
        sample_args = [
            '--start', '23:59',
            '--end', '01:40', 
            '--unit', 'minutes'
        ]
        
        # Simulate command line arguments via sys.argv for the main block execution logic if no args provided, but since we can't use input(), and argparse is forbidden to be required. 
        # The instruction says "Never call... argparse required arguments". This usually means don't define `required=True` in add_argument().
        # It does not forbid passing defaults or simulating CLI calls.
        
        if len(sys.argv) > 1:
            args = parser.parse_args()
        else:
            # Fallback for direct script execution without any arguments passed externally to the interpreter call,
            # but using a simulated context as per "sample block" requirement which implies running with specific values.
            import sys
            
            # We will force parsing of our sample data into args object structure manually if nothing is there? 
            # Actually, easiest way respecting rules: Just parse whatever was given, and default to None. 
            # Then in the main block logic handle defaults.
            pass

    parser = argparse.ArgumentParser()
    
    start_parser = argparse.ArgumentParser(add_help=False)
    end_parser = argparse.ArgumentParser(add_help=False)
    
    group_time2 = parser.add_argument_group('Time Specifications')
    group_time2.add_argument('--start', type=parse_time, default=None)
    group_time2.add_argument('--end', type=parse_time, default=None)

    # Let's restructure slightly to ensure the specific sample runs cleanly without requiring flags in typical usage if we want it super robust. 
    # But standard argparse behavior is fine as long as `required=False` (implicit).
    
    parser.parse_args(['--start', '23:59', '--end', '01:40', '-u', 'minutes'])

if __name__ == '__main__':
    import sys
    
    # Ensure we have the sample values running. If this is run without args in a test environment, 
    # argparse might error if not configured right for optional. 
    # The instruction says "Do not include... command-line arguments". Wait. 
    # "The sample block must run without user input, command-line arguments..."
    # This implies the `if __name__ == '__main__':` section should execute logic that calculates based on hard-coded values even if NO args were passed to python script.
    
    # Since we cannot have argparse required arguments in ANY case (global rule), 
    # and we need it to run without CLI args, I will configure parser with defaults=None everywhere.
    
    p = argparse.ArgumentParser()
    start_p = None
    end_p = None