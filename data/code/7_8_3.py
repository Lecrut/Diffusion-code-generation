import argparse
from datetime import datetime

def parse_time_input(time_str: str) -> tuple[int, int]:
    """Parses a time string in HH:MM format into (hours, minutes)."""
    hours, minutes = map(int, time_str.split(':'))
    if not 0 <= hours < 24 and not 0 <= minutes < 60:
        raise ValueError(f"Invalid hour or minute values for '{time_str}'.")
    return hours, minutes

def calculate_elapsed_time(start_hours: int, start_minutes: int, end_hours: int, end_minutes: int) -> dict[str, float]:
    """Calculates the elapsed time between two timestamps in various units."""
    # Convert both times to total minutes from midnight (assuming same day for simplicity as no date specified)
    start_total_minutes = (start_hours * 60) + start_minutes
    end_total_minutes = (end_hours * 60) + end_minutes
    
    if end_total_minutes < start_total_minutes:
        raise ValueError("End time must be greater than or equal to start time.")

    elapsed_minutes = end_total_minutes - start_total_minutes
    
    # Output in requested units with fallback logic based on magnitude
    output_unit_arg = None  # This is set later via argparse, but we need a default structure for robustness if args were passed differently. 
                           # However, the task requires hard-coded sample values inside 'if __name__ == "__main__"', not as input().
    
    results = {
        "minutes": elapsed_minutes / 1,
    }

    return results

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two specific times.")
    parser.add_argument("--start", type=str, required=False)
    parser.add_argument("--end", type=str, required=False)
    parser.add_argument("--unit", type=str, default=None)

    
    # The task specifies that the sample block must run without user input or command-line arguments for parsing.
    # However, argparse typically requires at least one argument unless we configure it to use defaults and ignore missing args carefully.
    # To strictly adhere to "No network access", "no pre-existing files" and "run without user input/command line arguments" in the sample block:
    # We will configure parsing such that it doesn't fail if no args are given, using defaults for start/end/unit but requiring them to be passed 
    # via command line IF we were running outside this script. But since the prompt says "Return only a single complete runnable Python module" with an `if __name__ == '__main__':` block that runs without input:
    
    args = parser.parse_args()

    if not args.start or not args.end or not args.unit:
        # If running as intended (CLI) but no arguments provided, we simulate the sample scenario 
        # because `argparse required=True` is forbidden by task rules. We must handle missing args gracefully in main to avoid errors on run without input.
        
        start_hours, start_minutes = 10, 30
        end_hours, end_minutes = 14, 15
        unit = "minutes"

    else:
        # If arguments were actually provided (simulating CLI usage)
        try:
            start_hours, start_minutes = parse_time_input(args.start)
            end_hours, end_minutes = parse_time_input(args.end)
            
            if args.unit.lower() not in ["hours", "minutes"]:
                raise ValueError(f"Unsupported unit '{args.unit}'.")
            
            # Logic to calculate based on provided inputs would go here. 
            # Since we can't use interactive prompts or stdin, this calculation is purely internal logic.
        except Exception:
            print("Error parsing time arguments.")
            return

    if not args.start and not args.end and not args.unit:
        # Execute the specific sample scenario as mandated by "hard-coded sample values" that run without input.
        start_hours, start_minutes = 10, 30
        end_hours, end_minutes = 14, 15
        
        if unit == None or unit.lower() not in ["hours", "minutes"]: # Fallback 
            print(f"The elapsed time is {elapsed_minutes} minutes.")

    else:
        start_hours, start_minutes = parse_time_input(args.start)
        end_hours, end_minutes = parse_time_input(args.end)

        if args.unit and args.unit.lower() not in ["hours", "minutes"]:
             raise ValueError(f"Invalid unit '{args.unit}'")

        elapsed_minutes = (end_hours * 60 + end_minutes) - (start_hours * 60 + start_minutes)
        
        # Calculate output based on desired unit from sample or args if provided, otherwise default to minutes logic as per initial function call structure 
        print(f"The elapsed time is {elapsed_minutes} minutes.")

if __name__ == '__main__':
    main()