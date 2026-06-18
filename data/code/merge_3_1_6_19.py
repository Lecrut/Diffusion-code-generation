class WeightConverter:
    """A class to handle weight conversions between different units."""
    
    # Conversion factors relative to kilograms
    FACTORS = {
        'kg': 1,
        'lb': 0.453592,
        'oz': 0.0283495,
        'tonne': 1000,
        'st': 6.35029 # stones to kg (approx)
    }

    def __init__(self, value: float, unit: str):
        """Initialize the converter with a weight value and its current unit."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float")
        self.value = abs(value) # Store absolute value for display consistency
        self.current_unit = unit.lower()

    def convert_to(self, target_unit: str):
        """Dynamically change the stored weight to the specified unit."""
        if not isinstance(target_unit, str):
            raise TypeError("Target unit must be a string")
        
        # Normalize units for lookup
        source_key = self.current_unit.lower()
        target_key = target_unit.lower()

        if source_key == '':
            raise ValueError(f"Invalid current unit: {self.current_unit}")
            
        factor_from_kg = self.FACTORS.get(source_key)
        factor_to_kg = self.FACTORS.get(target_key)

        if not factor_from_kg or not factor_to_kg:
            return None # Indicate unsupported units without raising error immediately, per dynamic requirement flexibility
            
        try:
            # Convert source to kg, then target from kg
            converted_value = (self.value * factor_from_kg / 1) * factor_to_kg
            self.current_unit = target_key
            self.value = abs(converted_value)
            return True
        except ZeroDivisionError:
            raise ValueError("Cannot convert between units with zero conversion factors")

    def get_weight(self):
        """Return the current stored weight value."""
        return self.value

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Convert from pounds (lb) to kilograms (kg)
    original_lb = WeightConverter(20.5, 'lb')
    print(f"Original weight: {original_lb.get_weight()} lbs")
    
    if original_lb.convert_to('kg'):
        converted_kg = original_lb.get_weight()
        print(f"Converted to kg: {converted_kg:.4f} kg")

    # Sample 2: Convert from kilograms (kg) back to pounds (lb), then ounces (oz)
    sample_2 = WeightConverter(10, 'kg')
    
    if sample_2.convert_to('lb'):
        lbs_val = sample_2.get_weight()
        print(f"Converted {sample_2.current_unit} value: {lbs_val:.4f}")

        # Chain conversion from lb to oz within the same object logic flow simulation
        original_lb.reset_value(lbs_val) # Helper concept handled via re-init for clarity in standalone script
        
    # Re-initializing specifically for the second chain demonstration as per class structure constraints
    sample_2b = WeightConverter(10, 'kg')
    
    if sample_2b.convert_to('lb'):
        lbs_value = sample_2b.get_weight()
        
        # Create a new instance from the calculated pounds to convert further to ounces
        oz_converter = WeightConverter(lbs_value, 'lb')
        
        if oz_converter.convert_to('oz'):
            final_oz = oz_converter.get_weight()
            print(f"Final conversion result: {final_oz:.4f} oz")

    # Sample 3: Invalid unit handling demonstration (optional silent fail)
    try:
        invalid_test = WeightConverter(5, 'invalid_unit')
        if invalid_test.convert_to('kg'):
            pass 
    except ValueError as ve:
        print(f"Error occurred during conversion: {ve}")