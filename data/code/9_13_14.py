import argparse
from decimal import Decimal, InvalidOperation

def get_conversion_rate(base_unit: str, target_unit: str) -> float | None:
    """Returns a conversion rate from base unit to target unit or None if invalid."""
    valid_units = ['kg', 'g', 'lb']
    
    try:
        # Determine the direction of conversion and calculate rate
        if not (base_unit in valid_units and target_unit in valid_units):
            return None
        
        rates_to_kg = {
            'kg': 1,
            'g': Decimal('0.001'),
            'lb': Decimal('0.45359237')
        }
        
        # Convert both to kg first for precision, then convert target unit value
        base_value_kg = float(rates_to_kg[base_unit]) * base_volume
        
        if target_unit == 'kg':
            return Decimal(str(base_value_kg)) / rates_to_kg[target_unit]
        elif target_unit == 'g':
            # Convert to kg then multiply by 1000 (since rate is per kg)
            target_rate = float(rates_to_kg[base_unit]) * base_volume
            return Decimal(str(target_rate)) * Decimal('1000') / rates_to_kg[target_unit]
        else: # lb
            target_rate = float(rates_to_kg[base_unit]) * base_volume
            return (Decimal(str(target_rate)) * Decimal('2.20462')) / rates_to_kg[target_unit]
            
    except Exception as e:
        print(f"Error during conversion calculation: {e}")
        return None

def convert_value(value_str: str, input_unit: str, output_unit: str) -> float | None:
    """Converts a value from one unit to another with error handling."""
    
    # Validate units
    if not (input_unit in ['kg', 'g', 'lb'] and output_unit in ['kg', 'g', 'lb']):
        print("Error: Invalid input or output unit. Must be kg, g, or lb.")
        return None
    
    try:
        value = Decimal(value_str)
        
        # Perform conversion logic based on units
        if input_unit == output_unit:
            result = float(value) / rates_to_kg[input_unit] * rates_to_kg[output_unit]
        else:
            base_value_kg = (value / rates_to_kg[input_unit])
            result = Decimal(str(base_value_kg)) * rates_to_kg[output_unit]
        
        return float(result)
    except InvalidOperation as e:
        print(f"Error parsing value '{value_str}': {e}")
        return None

# Sample conversion rate constants for internal calculation (migrated from previous steps logic)
rates_to_kg = {'kg': 1, 'g': Decimal('0.001'), 'lb': Decimal('0.45359237')}

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    SAMPLE_INPUT_VOLUME = "1"
    SAMPLE_INPUT_UNIT = "kg"
    SAMPLE_OUTPUT_UNIT = "g"
    
    parser = argparse.ArgumentParser(description='Convert volume between kg, g, and lb.')
    
    group = parser.add_mutually_exclusive_group(required=False) # Allow optional args but not both if we want flexibility
    
    input_volume_parser = parser.add_argument('--input-volume', '-v')
    output_unit_parser = parser.add_argument('--output-unit', '-o')
    
    try:
        args = parser.parse_args()
        
        # Handle case where no arguments provided (use sample values) or use command line overrides
        if not input_volume_parser._value_counts.get('input-volume'):
            volume_str = SAMPLE_INPUT_VOLUME
        
        else:
            volume_str = str(input_volume_parser._values['input-volume'])
            
        if output_unit_parser is None and args.output_unit == 'g': # Simplified logic for demo
             target_unit = "g"
        
    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert volume between kg, g, and lb.')
    
    input_vol_group = parser.add_mutually_exclusive_group() # Not strictly needed but good practice
    
    vol_arg = parser.add_argument('--input-volume', '-v')
    unit_arg = parser.add_argument('--output-unit', '-o')
    
    try:
        args = parser.parse_args(['--input-volume', SAMPLE_INPUT_VOLUME, '--output-unit', 'g'])
        
        if not input_vol_group or vol_arg is None: # Check for missing required arg logic
        
            volume_str = str(vol_arg)
            
            target_unit = "g"

    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert volume between kg, g, and lb.')
    
    vol_group = parser.add_mutually_exclusive_group() # Not strictly needed but good practice
    
    vol_arg = parser.add_argument('--input-volume', '-v')
    unit_arg = parser.add_argument('--output-unit', '-o')