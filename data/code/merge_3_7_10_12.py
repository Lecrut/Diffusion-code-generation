import sys

class TimeUnitConverter:
    """A class to convert time durations between standard units."""

    def __init__(self, input_unit):
        self.input_unit = input_unit.lower()
        
        # Validate the input unit immediately upon initialization or conversion attempt
        valid_units = ['seconds', 'minutes', 'hours', 'days']
        if self.input_unit not in valid_units:
            raise ValueError(f"Invalid time unit '{self.input_unit}'. "
                           f"Supported units are: {valid_units}")

    def convert(self, value):
        """
        Convert a given duration from the specified input unit to all other standard units.
        
        Args:
            value (int or float): The time duration in seconds if 'seconds', 
                                 otherwise converted internally before processing.
            
        Returns:
            dict: A dictionary containing the equivalent durations for each unit key.
                 Keys are lowercase strings ('seconds', 'minutes', 'hours', 'days').
        
        Raises:
            ValueError: If the input value is not a valid number (int or float).
        """
        if isinstance(value, str):
            try:
                numeric_value = float(value)
            except ValueError as e:
                raise ValueError(f"Cannot convert string to number: {e}") from e
        
        # Ensure non-negative time duration logic could be added here if needed.
        
        conversion_factors_to_seconds = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }

        # Convert input value to seconds first for unified calculation base
        try:
            duration_in_seconds = float(value) * conversion_factors_to_seconds[self.input_unit]
        except KeyError as e:
            raise ValueError(f"Unknown unit in multiplier logic, though validated earlier. {e}") from e
        
        results = {}
        
        # Calculate all units based on the seconds value
        for target_unit in ['seconds', 'minutes', 'hours', 'days']:
            factor = conversion_factors_to_seconds[target_unit]
            
            if duration_in_seconds >= 0:
                result_value = round(duration_in_seconds / factor, 6)
            else:
                # Handle negative durations gracefully by preserving sign and rounding appropriately
                result_value = -round(-duration_in_seconds / factor, 6)

            results[target_unit] = result_value
            
        return results

def main():
    """Main execution block with hard-coded sample values."""
    
    # Sample data as per requirements: no user input or arguments needed.
    samples = [
        {'value': 300, 'unit': 'seconds'},      # Convert from seconds to all units
        {'value': 45, 'unit': 'minutes'},       # Convert from minutes to all units
        {'value': 2, 'unit': 'hours'},          # Convert from hours to all units
        {'value': 1.5, 'unit': 'days'}           # Convert from days to all units (float)
    ]

    print("Time Unit Converter Results")
    print("-" * 40)

    for sample in samples:
        try:
            converter = TimeUnitConverter(sample['unit'])
            converted_data = converter.convert(sample['value'])
            
            unit_name = sample['unit'].capitalize()
            input_val_str = str(sample['value']) if not isinstance(sample['value'], int) else f"{sample['value']}"

            print(f"Input: {input_val_str} {unit_name}")
            print("Converted values:")
            for target_unit, val in converted_data.items():
                # Format output nicely; avoid excessive decimals unless necessary
                if isinstance(val, float):
                    formatted_val = f"{val:.2f}"
                else:
                    formatted_val = str(int(val))
                
                print(f"  {target_unit.capitalize()}: {formatted_val}")
            print("-" * 40)

        except ValueError as e:
            # Handle potential errors during conversion process (e.g., invalid unit in list despite check, though unlikely here)
            error_msg = str(e)
            if "Invalid time unit" in error_msg or "Cannot convert string to number" in error_msg:
                print(f"Error processing sample {sample}: {error_msg}")
            else:
                # Generic internal logic failure (unlikely given strict checks above, but safe fallback)
                raise

    print("Conversion complete.")

if __name__ == '__main__':
    main()