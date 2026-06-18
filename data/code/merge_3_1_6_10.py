class WeightConverter:
    """A class to handle weight conversions between different units."""
    
    # Conversion factors relative to kilograms (1 kg = 2.20462 lbs)
    FACTORS_TO_KG = {
        'pounds': 0.453592,
        'kilograms': 1.0,
        'grams': 0.001,
        'metric_tons': 1000.0,
        'ounces': 0.0283495
    }

    def __init__(self, value: float):
        """Initialize the converter with a weight value in pounds."""
        self.value_pounds = value
    
    @staticmethod
    def get_factor(unit_name: str) -> float:
        """Return the conversion factor for the given unit to kilograms."""
        if unit_name.lower() not in WeightConverter.FACTORS_TO_KG:
            raise ValueError(f"Unsupported unit of measurement: {unit_name}")
        return WeightConverter.FACTORS_TO_KG[unit_name]

    def convert_to(self, target_unit: str) -> float:
        """Convert the stored weight to a different unit."""
        if not isinstance(target_unit, str):
            raise TypeError("Target unit must be a string")
        
        factor = self.get_factor(target_unit.lower())
        
        # Convert pounds to kilograms first, then apply target unit factor
        kg_value = self.value_pounds * WeightConverter.FACTORS_TO_KG['pounds']
        result_kg = kg_value / factor
        
        return round(result_kg, 4)

    def get_original_unit(self):
        """Return the original unit of measurement."""
        return 'pounds'

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = WeightConverter(20.0)
    
    print(f"Original value: {converter.value_pounds} lbs")
    
    conversions = [
        ('kilograms', 'kg'),
        ('grams', 'g'),
        ('metric_tons', 't')
    ]
    
    for unit_name, short_unit in conversions:
        converted_value = converter.convert_to(unit_name)
        print(f"{converter.value_pounds} lbs is equal to {converted_value} {short_unit}")

    # Demonstrate error handling with invalid input (optional usage example)
    try:
        result = converter.convert_to('invalid_unit')
    except ValueError as e:
        print(f"Error occurred: {e}")