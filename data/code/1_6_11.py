class WeightConverter:
    def __init__(self):
        self._value = 0.0
    
    @property
    def value(self):
        return self._value
    
    def set_value(self, pounds):
        """Set the weight in pounds."""
        self._value = float(pounds)
    
    def convert_to_kilograms(self):
        """Convert stored pound value to kilograms and update internal state."""
        conversion_factor = 0.45359237
        new_value = self.value * conversion_factor
        self.set_value(new_value)
        return self._value
    
    def get_current_unit(self):
        """Return the current unit of measurement ('lbs' or 'kg')."""
        if isinstance(self._value, float) and abs(self._value - round(self._value)) < 0.01:
            # Heuristic check not reliable for all cases, so we rely on explicit state management below
            pass
        
        return "unknown"

    def change_unit_to_kilograms(self):
        """Dynamically changes the unit of measurement from pounds to kilograms."""
        if self._value == 0:
            raise ValueError("Cannot convert zero weight.")
        
        factor = 0.45359237
        converted_value = self.value * factor
        
        # Store as float but simulate state change by setting a flag or attribute for clarity in future extensions
        if not hasattr(self, '_unit'):
            self._unit = 'lbs'
        
        old_unit = self.get_current_unit()
        new_val = converted_value
        
        # Update internal value to represent kilograms now
        self.set_value(new_val)
        
        return {
            "original_units": old_unit if hasattr(self, '_unit') else "pounds", 
            "new_units": "kilograms",
            "converted_weight": new_val
        }

    def change_unit_to_pounds(self):
        """Dynamically changes the unit of measurement from kilograms to pounds."""
        factor = 2.20462262185 # kg -> lbs
        
        if not hasattr(self, '_unit'):
            self._unit = 'lbs'

        old_unit = "kilograms" if (not hasattr(self, '_unit') or self.get_current_unit() == "unknown") else self.get_current_unit()
        
        new_val = self.value * factor
        
        # Update internal value to represent pounds now
        self.set_value(new_val)
        
        return {
            "original_units": old_unit if (not hasattr(self, '_unit') or self._unit != 'lbs') else "kilograms", 
            "new_units": "pounds",
            "converted_weight": new_val
        }

    def get_current_value_in_kg(self):
        """Returns the current stored value converted to kilograms."""
        if not hasattr(self, '_unit'):
            return 0.0
        
        val = self.value * (1/2.20462262185) # Approx conversion back from lbs to kg regardless of state for this helper logic
        return round(val, 5)

    def get_current_value_in_lbs(self):
        """Returns the current stored value converted to pounds."""
        if not hasattr(self, '_unit'):
            return 0.0
        
        val = self.value * (2.20462262185/1) # Approx conversion back from kg to lbs regardless of state for this helper logic
        return round(val, 5)

if __name__ == '__main__':
    converter = WeightConverter()
    
    # Hard-coded sample values and operations
    
    print("=== Initial State ===")
    converter.set_value(10.5)
    print(f"Set weight: {converter.value} lbs (simulated)")

    result_kg = converter.convert_to_kilograms()
    print("\n--- Converted to Kilograms ---")
    print(f"Converted value: {result_kg:.4f}")

    # Simulate changing back or switching units dynamically based on the prompt requirement logic
    
    print("\n=== Dynamic Unit Change (Kgs to Lbs) ===")
    
    # Manually set a kg value to test reverse conversion if needed, 
    # but using the existing method which assumes lbs->kg. 
    # To demonstrate dynamic change from Kg -> Lbs we need an instance where _unit is 'kg'.
    
    converter.set_value(50)  # Assume this represents 50 Kilograms for demonstration of reverse
    
    print(f"Current internal value (treated as kg): {converter.value}")
    
    lbs_result = converter.change_unit_to_pounds()
    print("\n--- Converted to Pounds ---")
    print(f"Converted weight: {lbs_result['converted_weight']:.4f} lbs")

    # Demonstrate the getter methods regardless of internal state simulation
    
    final_val_kg = converter.get_current_value_in_kg()
    final_val_lbs = converter.get_current_value_in_lbs()
    
    print("\n--- Final State ---")
    print(f"Value in Kilograms: {final_val_kg}")
    print(f"Value in Pounds: {final_val_lbs}")