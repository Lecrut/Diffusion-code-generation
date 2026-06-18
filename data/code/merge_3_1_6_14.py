class WeightConverter:
    """A class to handle weight conversions between different units."""
    
    # Conversion factors relative to kilograms (1 kg = 2.20462 lbs)
    FACTORS = {
        'pounds': 1,
        'kilograms': 1 / 2.20462,
        'grams': 3527.4, # grams per pound * pounds factor for simplicity in this context relative to lb input
        'ounces': 32,    # ounces per pound
    }

    def __init__(self, value: float):
        """Initialize the converter with a weight value."""
        self.value = abs(value)

    @staticmethod
    def convert_from_pounds_to_kilograms(pounds: float) -> float:
        """Convert pounds to kilograms using standard conversion factor."""
        return pounds * 0.45359237

    @classmethod
    def change_unit(cls, current_value: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
        """
        Dynamically changes the unit of measurement for a stored weight value.
        
        Args:
            current_value (float): The original weight value in pounds.
            from_unit (str): Source unit ('pounds').
            to_unit (str): Target unit ('kilograms', 'grams', etc.).

        Returns:
            tuple[float, dict]: A tuple containing the converted value and a history dictionary.
        
        Raises:
            ValueError: If unsupported units are provided or conversion fails.
        """
        # Ensure input is valid pounds as per problem context (dynamic change from stored lb)
        if current_value < 0:
            raise ValueError("Weight cannot be negative.")

        converted_val = cls.convert_from_pounds_to_kilograms(current_value)
        
        history = {
            'original_unit': 'pounds',
            'original_value': current_value,
            'conversion_factor_used': 1 / 2.20462 if to_unit == 'kilograms' else 
                         (cls.convert_from_pounds_to_kilograms(current_value) * cls.FACTORS[to_unit]) if to_unit in ['grams', 'ounces'] else None, # Simplified logic for demo
            'final_value': converted_val if to_unit == 'kilograms' else 0.0 # Placeholder for other units calculation below
        }

        # Recalculate final value based on target unit relative to the base kg result
        history['conversion_factor_used'] = cls.FACTORS.get(to_unit, None) * (1 / 2.20462 if from_unit == 'pounds' else 1)
        
        if to_unit in ['kilograms', 'grams', 'ounces']:
            # Convert the base kg value to target unit
            final_val = converted_val * cls.FACTORS.get(to_unit, None) or (converted_val / 2.20462) 
            history['final_value'] = final_val if to_unit == 'kilograms' else final_val
        
        return float(history['final_value']), history

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    
    converter_instance = WeightConverter(10.5)

    result, details = WeightConverter.change_unit(converter_instance.value, 'pounds', 'kilograms')
    
    print(f"Original Value: {converter_instance.value} pounds")
    print(f"Converted to Kilograms: {result:.4f}")
    print("Conversion Details:", details['conversion_factor_used'])

    # Example with another unit for demonstration within the same structure logic
    result_grams, details_g = WeightConverter.change_unit(converter_instance.value, 'pounds', 'grams')
    
    print(f"Converted to Grams: {result_grams:.4f}")