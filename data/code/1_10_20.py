import csv

def parse_weight(value):
    """Convert a string value to float."""
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(f"Non-numeric entry found in weight data: '{value}'. Error details: {e}") from e

def calculate_average(weights):
    """Calculate the average of the provided list of weights."""
    if not weights:
        return 0.0
    
    total = sum(weights)
    return total / len(weights)

if __name__ == '__main__':
    # Hard-coded sample data simulating a CSV file content
    # Format: weight, height (we only care about the first column for this task)
    raw_data = [
        "70.5",      # Valid float
        "68.2",      # Valid float
        "invalid",   # Invalid entry to test error handling
        "71.9",      # Valid float
        "abc"        # Another invalid entry
    ]

    weights = []

    try:
        for row in raw_data:
            weight_str = row.strip()
            if not weight_str or weight_str.startswith('#'):  # Skip empty lines and comments
                continue
            
            parsed_weight = parse_weight(weight_str)
            weights.append(parsed_weight)

        average_weight = calculate_average(weights)
        
        print(f"Average Weight: {average_weight}")
    
    except ValueError as e:
        print(f"Error processing data: {e}", file=__import__('sys').stderr)