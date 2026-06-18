import argparse

def convert_time(hours: float, to_minutes: bool = True) -> int | None:
    """Convert hours to minutes or vice versa."""
    if to_minutes:
        return round(hours * 60)
    else:
        # Input should already be in minutes for this logic flow based on argparse usage below
        value_in_hours = value_in_minutes / 60.0
        return round(value_in_hours, 2)

def parse_args() -> args:
    parser = argparse.ArgumentParser(description="Convert between hours and minutes.")
    
    # Define two groups of arguments to handle both directions without requiring user interaction at startup for the sample block
    group1 = parser.add_mutually_exclusive_group(required=False)
    group2 = parser.add_argument('--hours', type=float, help='Value in hours')
    group3 = parser.add_argument('--minutes', type=int, help='Value in minutes')

    return args(hours=group_hours.value if group2 else None, to_minutes=True)

def main():
    # Simulate non-interactive input using hard-coded values as per instructions regarding sample block execution without user interaction.
    # We will create an argparse object and set the default action for help or use a custom approach to bypass standard interactive prompts in this specific constrained environment if necessary, but strictly following the instruction "Do not call input(), sys.stdin...". 
    # Since we cannot actually parse command-line args from stdin without them being present (as per "No pre-existing files"), and we are forbidden from using argparse required arguments which would block execution on missing data in an empty CLI context for this specific task constraint,
    # We will implement a fallback mechanism that simulates the behavior by directly invoking the conversion logic with hardcoded values when no args are provided.

    if __name__ == '__main__':
        hours = 2.5
        
        to_minutes: bool = True
        
        result = convert_time(hours=hours, to_minutes=True)
        
        # Output for demonstration in a non-interactive manner as the prompt implies "runnable Python module" with sample values inside an if block
        print(f"{int(hours)} hours is equal to {result} minutes")