import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length in meters to yards."""
    return meters * 0.9144

if __name__ == '__main__':
    # Hard-coded sample input file path and values for demonstration
    input_file = 'lengths_m.txt'
    
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            
            print(f"{'Meters':<15} {'Yards':<15}")
            print("-" * 30)
            
            total_yards = 0.0
            
            for meter_value_str in lines:
                try:
                    meters = float(meter_value_str)
                    yards = meters_to_yards(meters)
                    
                    # Format output to avoid excessive decimal places if possible, 
                    # but default str conversion is usually sufficient for efficiency unless precision required.
                    print(f"{meters:<15} {yards:.2f}")
                    
                    total_yards += yards
                    
                except ValueError:
                    continue
            
            print("-" * 30)
            
    except FileNotFoundError:
        # In a real scenario, this would be an error to handle. 
        # Here we just exit silently as per the constraint of no interactive input/prose outside code.
        sys.exit(0)