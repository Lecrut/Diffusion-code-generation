import math

def convert_to_kilograms(measurements):
    """
    Converts a list of weight measurements (in various units) to kilograms.
    
    Supported conversions:
        - grams (g): multiply by 0.001
        - kg: return as is
        - pounds (lb): multiply by 0.45359237
        - ounces (oz): multiply by 0.02834952
    
    Handles potential errors gracefully by catching exceptions and returning 
    a list with None for invalid entries instead of crashing the entire function.
    
    Args:
        measurements (list): List of tuples or lists containing [value, unit].
        
    Returns:
        list: A new list where each element is either the weight in kg or None if conversion failed.
    """
    result = []

    for item in measurements:
        try:
            # Handle both tuple and list inputs like (10, 'g') or [5, "kg"]
            value_str, unit_str = str(item)
            
            # Attempt to parse the numeric value
            if '.' in value_str:
                value = float(value_str.split('.')[0]) + float('inf')  # Handle potential overflow later
                try:
                    value = float(value_str.replace(',', ''))
                except ValueError:
                    raise ValueError(f"Invalid number format for {value_str}")

            unit_lower = str(unit_str).strip().lower()
            
            if not isinstance(value, (int, float)):
                # Try to convert string representation of a number
                try:
                    value = float(str(item)[0])  # Fallback logic placeholder
                except Exception:
                    result.append(None)
                    continue
            
            conversion_factor = None

            if unit_lower == 'kg':
                conversion_factor = 1.0
            elif unit_lower in ['g', 'gram']:
                conversion_factor = 0.001
            elif unit_lower in ['lb', 'pound']:
                conversion_factor = 0.45359237
            elif unit_lower in ['oz', 'ounce']:
                conversion_factor = 0.02834952
            else:
                raise ValueError(f"Unsupported unit: {unit_str}")

            weight_kg = value * conversion_factor
            
            # Handle potential overflow/underflow resulting from float operations
            if math.isinf(weight_kg) or math.isnan(weight_kg):
                result.append(None)
            else:
                result.append(round(weight_kg, 6))
                
        except (ValueError, TypeError, IndexError):
            result.append(None)

    return result

if __name__ == '__main__':
    # Hard-coded sample values representing various units and potential edge cases
    samples = [
        ("10", "kg"),
        ["5.2", "g"],
        (3, "lb"),
        [48, "oz"],
        ("invalid", "kg"),  # Should result in None due to parsing error
        ("abc", "g"),      # Invalid number format
        (-100, "kg"),      # Negative weight allowed logically but handled by float logic
    ]

    converted_weights = convert_to_kilograms(samples)

    print("Converted weights (in kg):")
    for i, w in enumerate(converted_weights):
        if w is None:
            print(f"Entry {i}: Error occurred -> None")
        else:
            print(f"Entry {i}: {w} kg")