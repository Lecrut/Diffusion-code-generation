import math

class WeightConverter:
    """A class to handle weight value conversions between different units."""
    
    # Conversion factors relative to kilograms (1 kg = 2.20462 lbs)
    CONVERSION_FACTORS = {
        'pounds_to_kg': lambda val: val / 2.20462,
        'kg_to_pounds': lambda val: val * 2.20462,
        'ounces_to_kg': lambda val: val / (16 * 2.20462),
        'lb_to_oz': lambda val: val * 16,
    }

    def convert(self, value_in_units: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
        """
        Dynamically converts a weight value from one unit to another.
        
        Parameters:
            value_in_units (float): The numeric weight value in the source unit.
            from_unit (str): The source unit string ('pounds', 'kg', 'ounces').
            to_unit (str): The target unit string ('kilograms', 'lb', 'oz').
            
        Returns:
            tuple[float, dict]: A tuple containing the converted value and a dictionary 
                              with metadata including original input, conversion factor used.
        
        Raises:
            ValueError: If an unsupported unit is provided or invalid argument types are detected.
        """
        supported_units = {'pounds', 'kg'}
        if from_unit not in supported_units:
            raise ValueError(f"Unsupported source unit: {from_unit}. Supported units are {supported_units}")

        supported_targets = ['kilograms', 'lb']
        if to_unit == 'lb':
            target_key = 'pounds_to_kg' # Logic handles conversion via kg as intermediate or direct mapping below
            
        elif to_unit in {'kg'}:
            target_key = None # Default logic assumes standard conversions
        
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}. Supported units are {supported_targets}")

        if from_unit == 'pounds':
            factor = 1 / 2.20462
            
        elif from_unit == 'kg':
            factor = 2.20462
        
        else:
            raise ValueError(f"Unsupported source unit type")

        converted_value = value_in_units * factor

        if to_unit in {'lb'}: # Convert back to pounds specifically requested
             return (value_in_units, { "original": f"{value_in_units} lbs", "converted": round(converted_value, 4), 
                                      "factor_used": 1 / 2.20462 })

        elif from_unit == 'pounds' and to_unit in {'kg'}:
            return (round(value_in_units * factor, 4), { "original": f"{value_in_units} lbs", "converted": converted_value})

if __name__ == '__main__':
    # Hard-coded sample values execution without user input or external dependencies
    
    converter = WeightConverter()

    # Sample 1: Convert pounds to kilograms
    result_1, metadata_1 = converter.convert(20.5, 'pounds', 'kilograms')
    print(f"Input: {metadata_1['original']}")