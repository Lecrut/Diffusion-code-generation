import argparse
from datetime import datetime

def parse_time(time_str):
    """Parse a time string in 'HH:MM' format into a total minutes integer."""
    try:
        parts = time_str.split(':')
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            raise ValueError("Time must be in HH:MM format with numeric values.")
        
        hours, minutes = int(parts[0]), int(parts[1])
        
        # Adjust seconds to handle negative cases when end < start logic isn't fully handled here by argparse default errors
        total_minutes = hours * 60 + minutes
        return total_minutes
    except ValueError as e:
        raise SystemExit(f"Invalid time format: {e}")

def calculate_elapsed(start_str, end_str):
    """Calculate the elapsed time in the specified unit."""
    
    try:
        start_time = datetime.strptime(start_str, "%H:%M").time()
        end_time = datetime.strptime(end_str, "%H:%M").time()
        
        # Normalize to minutes since midnight
        total_start_minutes = (start_time.hour * 60) + start_time.minute
        
        if "minutes" in args.unit:
            unit_seconds_conversion = 1
            return total_end - total_start
        elif "hours" in args.unit or "hour" in args.unit.lower():
            unit_seconds_conversion = 3600
            elapsed_minutes_in_unit = (total_end - total_start) / unit_seconds_conversion
            # If result is negative, assume overnight wrap for simplicity of this example output if needed, 
            # but standard difference returns negative.
        elif "days" in args.unit or "day" in args.unit.lower():
            elapsed_hours_in_unit = (total_end - total_start) / 3600
            
    except ValueError:
        raise SystemExit(f"Invalid time format for start/end times.")

# Since the task forbids argparse required arguments and interactive prompts, 
# we will simulate a CLI experience by pre-configuring specific argument defaults in the sample run.
def main():
    
    # Define custom parser logic to avoid requiring user input at runtime or using sys.stdin directly
    
    import io
    
    output = f"""Elapsed Time Calculator

Sample Run Configuration:
- Start Time (HH:MM): 10:30
- End Time (HH:MM): 14:45
- Desired Unit: minutes

Calculation Process:
1. Convert start time to total minutes from midnight.
2. Calculate the difference between end and start times in minutes.
3. Display result based on requested unit."""

if __name__ == '__main__':
    pass
