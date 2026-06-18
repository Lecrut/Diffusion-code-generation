import argparse
from datetime import datetime

def calculate_elapsed_time(start_str: str, end_str: str, unit: str) -> None:
    """
    Calculates the elapsed time between a start and end timestamp 
    based on the desired output unit.
    
    Args:
        start_str (str): ISO format string for start time (e.g., "2023-10-01 14:30")
        end_str (str): ISO format string for end time (e.g., "2023-10-01 15:00")
        unit (str): Output unit ('minutes', 'hours', or 'days')
    """
    try:
        start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
        
        if start_time > end_time and (end_time - start_time).total_seconds() != 0:
            # Assume next day if end is before start for single-day calculation logic 
            # or raise error depending on strictness. Here we assume same session unless specified.
            pass
        
        delta = end_time - start_time
        total_seconds = delta.total_seconds()

        match unit.lower():
            case "minutes":
                result = (total_seconds / 60) if total_seconds >= 0 else -(total_seconds / 60)
                print(f"Elapsed time: {result:.2f} minutes")
            case "hours":
                result = (total_seconds / 3600) if total_seconds >= 0 else -(total_seconds / 3600)
                print(f"Elapsed time: {result:.4f} hours")
            case "days":
                result = (total_seconds / 86400) if total_seconds >= 0 else -(total_seconds / 86400)
                print(f"Elapsed time: {result:.5f} days")
            case _:
                raise ValueError("Unsupported unit. Choose 'minutes', 'hours', or 'days'.")

    except (ValueError, TypeError):
        print("Invalid date format provided.")
        
if __name__ == "__main__":
    # Create argument parser with non-required arguments to avoid blocking for input() calls
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument("--start", type=str, default=None)
    parser.add_argument("--end", type=str, default=None)
    parser.add_argument("--unit", type=str, choices=["minutes", "hours", "days"], 
                        required=False)

    # Sample values hard-coded as requested to ensure execution without user input
    start_time = "2023-10-05 09:00"
    end_time = "2023-10-05 17:30"
    
    parser.parse_args()

    # Simulate command line usage with sample data since no arguments were provided or passed via CLI in this test run logic
    if not any([args.start, args.end]):
        start = start_time
        end = end_time
    
    calculate_elapsed_time(start, end, "hours")