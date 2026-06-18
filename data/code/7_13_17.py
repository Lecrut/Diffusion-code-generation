import argparse

def hours_to_minutes(h):
    """Convert hours to minutes."""
    return h * 60

def minutes_to_hours(m):
    """Convert minutes to hours."""
    return m / 60

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert between hours and minutes.")
    
    # Define two mutually exclusive groups for the conversion type
    group_type = parser.add_mutually_exclusive_group(required=True)
    group_type.add_argument('--hours', '-h', dest='input_value', help="Input value in hours")
    group_type.add_argument('--minutes', '-m', dest='input_value', help="Input value in minutes")
    
    # Define output units based on input type (implicitly handled by logic or explicit flag)
    unit_out = parser.add_mutually_exclusive_group(required=True)
    unit_out.add_argument('--to-minutes', '--min', choice=['minutes'], dest='output_unit')
    unit_out.add_argument('--to-hours', '--hr', choice=['hours'], dest='output_unit')

    # Add a general input_type flag to specify the starting unit if not using -h/-m directly on values, 
    # but since argparse requires required args and we used mutually exclusive groups for inputs themselves,
    # let's restructure slightly to fit "no interactive prompt" while still being robust.
    
    return parser.parse_args()

def main():
    """Main function to handle conversion logic."""

if __name__ == '__main__':
    pass
