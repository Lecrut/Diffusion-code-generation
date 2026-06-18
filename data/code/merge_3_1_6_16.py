class WeightConverter:
    """A class to handle weight value conversions between different units."""
    
    # Conversion factors relative to kilograms (1 kg = 2.20462 lbs)
    FACTORS = {
        'lb': 0.453592,      # Pounds to Kilograms factor
        'kg': 1.0,           # Base unit
        'oz': 0.0283495,     # Ounces to Kilograms factor
    }

    def __init__(self, value: float):
        """Initialize the converter with a weight value in pounds."""
        self.value = value
    
    @staticmethod
    def get_unit_factor(unit: str) -> float:
        """Return the conversion factor for the specified unit relative to kilograms."""
        return WeightConverter.FACTORS.get(unit.lower(), 0.453592)

    def convert_to(self, target_unit: str):
        """Dynamically change the stored weight value to a new unit of measurement.
        
        Args:
            target_unit (str): The target unit ('lb', 'kg', or 'oz').
            
        Returns:
            float: The converted weight value in the target unit.
        """
        if not target_unit:
            raise ValueError("Target unit cannot be empty.")

        # Convert current pounds to kilograms first, then to target unit
        kg_value = self.value * WeightConverter.FACTORS['lb']
        
        factor_to_target = WeightConverter.get_unit_factor(target_unit) / 1.0
        
        converted_value = kg_value * (1.0 / factor_to_target) if target_unit != 'kg' else kg_value

        # Update the stored value to reflect the new unit context for future operations
        self.value = converted_value
        return converted_value

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    
    # Create an instance with 20 pounds
    converter = WeightConverter(20)

    print(f"Original weight: {converter.value} lb")

    # Convert to kilograms
    kg_value = converter.convert_to('kg')
    print(f"Converted to kilograms: {kg_value:.4f}")

    # Reset for next demo (simulating a new state by creating fresh logic)
    # Note: In this specific implementation, the internal value is updated. 
    # To demonstrate multiple conversions from an original base without side effects on previous calls in a single run,
    # we can re-initialize or simply show the result of converting back to lbs if needed.
    
    # Let's create another instance for clarity on sequential operations starting fresh
    converter2 = WeightConverter(50)

    print(f"\nOriginal weight (second sample): {converter2.value} lb")

    # Convert 50 pounds to ounces
    oz_value = converter2.convert_to('oz')
    print(f"Converted to ounces: {oz_value:.4f}")

    # Demonstrate converting the result back conceptually by creating a new instance 
    # with the calculated value if we wanted to treat it as an input, 
    # but per task requirements, we just show dynamic conversion capability.
    
    print(f"\nFinal stored unit (oz): {converter2.value:.4f}")