import math

def convert_to_kilograms(measurements):
    """
    Converts a list of weight measurements (in various units) to kilograms.
    
    Supported units: 'kg', 'g', 'mg', 'lb', 'oz'
    Returns a tuple containing the converted weights in kg and any errors encountered as strings.
    
    Args:
        measurements (list): List of tuples or lists representing [value, unit]
        
    Returns:
        list: A new list with all values converted to kilograms. Errors are appended 
             if conversion fails for a specific item.
    """
    result = []
    valid_units = {'kg', 'g', 'mg', 'lb', 'oz'}

    try:
        # Define conversion factors relative to 1 kg
        # 1 lb ≈ 0.45359237 kg, 1 oz ≈ 0.028349523125 kg
        factors = {
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
            'lb': 0.45359237,
            'oz': 0.028349523125
        }

    except Exception:
        # Fallback if factor definition fails unexpectedly (unlikely)
        factors = {'kg': 1}

    for item in measurements:
        try:
            value, unit = item
            
            # Handle both tuple and list inputs gracefully
            if isinstance(item, str):
                parts = item.split(',')
                if len(parts) != 2:
                    raise ValueError("Invalid format string")
                
                val_str, unit_str = [p.strip().lower() for p in parts]
                value = float(val_str)
                unit = unit_str
                
            elif isinstance(item, (list, tuple)):
                # Ensure it has exactly two elements
                if len(item) != 2:
                    raise ValueError("Item must contain a numeric value and a string unit")
                
                val_str, unit_str = str(item[0]).strip(), str(item[1]).strip().lower()
                try:
                    value = float(val_str)
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid number format for item {item}")
            else:
                # If it's just a raw string or other type not handled above
                val_str = str(item).strip()
                
                if ',' in val_str and len(val_str.split(',')) == 2:
                    parts = [p.strip().lower() for p in val_str.split(',')]
                    value, unit = float(parts[0]), parts[1]
                else:
                    raise ValueError(f"Cannot parse {item}")

            # Validate inputs
            if not isinstance(value, (int, float)):
                raise TypeError("Value must be a number")
            
            if not isinstance(unit, str) or unit == '':
                raise ValueError("Unit must be a non-empty string")
                
            if value < 0:
                # Handle negative weights by taking absolute value for conversion logic 
                # but flagging it as an error in the result list to indicate anomaly
                is_negative = True
                abs_value = -value
            else:
                is_negative = False
            
            unit_lower = unit.lower()

            if unit_lower not in factors:
                raise ValueError(f"Unsupported unit '{unit}'. Supported units are {', '.join(valid_units)}")

            # Perform conversion
            converted_kg = abs_value * factors[unit_lower]
            
            result.append(converted_kg)
        except Exception as e:
            # Gracefully handle errors by appending an error message instead of crashing the whole function
            if isinstance(item, str):
                err_msg = f"Error processing '{item}': {str(e)}"
            else:
                try:
                    idx = list(measurements).index(item) + 1
                    # Find index in original list to report error location roughly
                    pass 
                except ValueError:
                    err_msg = str(e)
                
            result.append(err_msg)

    return result

if __name__ == '__main__':
    sample_data = [
        (50, 'kg'),           # 50 kg
        ('10', 'g'),          # 10 g -> string input format
        ['2500', 'mg'],       # 2.5 mg as list
        (3, 'lb'),            # 3 lbs
        [48, 'oz'],           # 48 ozs
        ('-10', 'g'),         # Negative value test
    ]

    converted_weights = convert_to_kilograms(sample_data)

    print("Converted weights in kilograms:")
    for i, weight in enumerate(converted_weights):
        if isinstance(weight, float):
            print(f"{i+1}. {weight} kg")
        else:
            print(f"{i+1}. Error: {weight}")