import json
from pathlib import Path

def read_volume_measurements(file_path: str) -> list[float]:
    """Reads a list of volume measurements (in liters or arbitrary units to be converted) from a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            # Attempt to parse as JSON first for structured lists like [10.5, 20]
            if content.startswith('['):
                measurements = json.loads(content)
                
                # Validate that the result is a list of numbers
                if not isinstance(measurements, list) or not all(isinstance(m, (int, float)) for m in measurements):
                    raise ValueError("JSON must contain only numeric values.")
            else:
                # Fallback to parsing as space-separated line(s)
                raw_values = content.split()
                
                try:
                    measurements = [float(x) for x in raw_values]
                except ValueError as e:
                    raise ValueError(f"Invalid input format containing non-numeric data.") from e
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except json.JSONDecodeError:
        raise ValueError("Input is not valid JSON and cannot be treated as space-separated values.")
    
    return measurements

def convert_to_cubic_meters(liters: float) -> float:
    """Converts a volume in liters to cubic meters."""
    # 1 liter = 0.001 cubic meter
    return liters * 0.001

if __name__ == '__main__':
    # Hard-coded sample values simulating file content
    input_data_str = "[5, 12.5, 300]"
    
    try:
        measurements_liters = [float(x) for x in input_data_str.strip('[]').split(',')] if ']' in input_data_str else eval(input_data_str)
        
        print(f"Input Volume (Liters): {measurements_liters}")
        
        cubic_meters_list = []
        print("Converted Measurements:")
        for val in measurements_liters:
            m3_val = convert_to_cubic_meters(val)
            cubic_meters_list.append(m3_val)
            
            # Formatting to avoid excessive decimals unless integer-like
            if m3_val == int(m3_val):
                formatted_str = f"{int(m3_val)}"
            else:
                formatted_str = f"{m3_val:.6f}"
                
            print(f"- {val} liters -> {formatted_str} cubic meters")
            
        # Print summary list if needed or as requested for completeness of "print equivalent measurements"
    except Exception as e:
        print(f"Error processing data: {e}")